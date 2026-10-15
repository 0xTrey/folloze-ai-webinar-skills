#!/usr/bin/env python3
"""Check a documented next-call budget snapshot offline. No provider calls or writes."""

import json
import sys
from decimal import Decimal, InvalidOperation
from pathlib import Path


def amount(value):
    if isinstance(value, bool) or value is None:
        raise ValueError("Amount must be a known nonnegative number")
    try:
        result = Decimal(str(value))
    except (InvalidOperation, ValueError) as error:
        raise ValueError("Amount must be a known nonnegative number") from error
    if not result.is_finite() or result < 0:
        raise ValueError("Amount must be a known nonnegative number")
    return result


def check(snapshot):
    """Validate declared readiness and arithmetic; do not grant execution authority."""
    reasons = []
    if not isinstance(snapshot, dict):
        return {"fits": False, "reasons": ["Snapshot must be an object"]}
    for key in (
        "scope_authorized", "operation_verified", "cost_verified", "balance_fresh",
        "overage_resolved", "shared_pool_coordinated", "record_and_rate_limits_fit",
    ):
        if snapshot.get(key) is not True:
            reasons.append(f"{key} is not verified true")
    for key in ("map_version", "route_id", "approval_ref", "cost_ref", "balance_ref"):
        if not isinstance(snapshot.get(key), str) or not snapshot[key].strip():
            reasons.append(f"{key} is missing")
    if snapshot.get("unresolved_call") is not False:
        reasons.append("Unresolved or unknown call outcome")
    proposed = snapshot.get("next_call", {})
    constraints = snapshot.get("constraints", [])
    if not isinstance(proposed, dict) or not proposed:
        reasons.append("Next-call upper bounds are missing")
        proposed = {}
    if not isinstance(constraints, list) or not constraints:
        reasons.append("Budget constraints are missing")
        constraints = []
    capacities = []
    for key, debit in proposed.items():
        # Key format keeps a pool's credits and money in distinct dimensions.
        if not isinstance(key, str) or len(key.split("|")) != 2 or any(not part for part in key.split("|")):
            reasons.append("Every bound needs a pool|unit key")
            continue
        try:
            charge = amount(debit)
        except ValueError:
            reasons.append(f"Unknown or invalid upper bound for {key}")
            continue
        relevant = [row for row in constraints if isinstance(row, dict) and row.get("key") == key]
        required = {"provider", "pool", "task"}
        scopes = [row.get("scope") for row in relevant]
        if any(not isinstance(scope, str) for scope in scopes) or set(scopes) != required or len(relevant) != 3:
            reasons.append(f"{key} needs one provider, pool, and task constraint")
            continue
        for row in relevant:
            try:
                remaining = amount(row.get("cap")) - amount(row.get("spent")) - amount(row.get("reserved"))
            except ValueError:
                reasons.append(f"Unknown or invalid allowance for {key}/{row['scope']}")
                continue
            capacities.append({"key": key, "scope": row["scope"], "remaining": str(remaining)})
            if charge > remaining:
                reasons.append(f"Next call exceeds {key}/{row['scope']} remaining allowance")
    if snapshot.get("all_billing_dimensions_included") is not True:
        reasons.append("Billing dimensions are incomplete or unknown")
    return {
        "fits": not reasons,
        "reasons": reasons,
        "remaining_before_call": capacities,
        "limits": "Checks declared inputs only; no reservation, provider enforcement, or permission grant",
    }


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 check_tool_budget.py next-call.json", file=sys.stderr)
        return 2
    try:
        snapshot = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
        result = check(snapshot)
    except (OSError, ValueError, TypeError) as error:
        result = {"fits": False, "reasons": [f"Invalid snapshot: {type(error).__name__}"]}
    print(json.dumps(result, indent=2))
    return 0 if result["fits"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
