#!/usr/bin/env python3
"""Read-only PNG dimensions, copy and board-link checks for an ad handoff."""
import argparse
import json
from pathlib import Path
import struct
from urllib.parse import parse_qs, urlsplit

SIZES = {(160, 600), (300, 250), (300, 600), (320, 480), (320, 50), (728, 90)}
IDENTITY = {'em', 'fn', 'ln', 'co', 'ro', 'token', 'recipient_id', 'contact_id'}


def check_exports(manifest, folder):
    if not isinstance(manifest, dict) or not isinstance(manifest.get('creatives'), list) or not manifest['creatives']:
        raise ValueError('Manifest needs a nonempty creatives list')
    base = urlsplit(manifest.get('destination_url', ''))
    errors, warnings, ids = [], [], set()
    boundary = Path(folder).resolve()
    for row in manifest['creatives']:
        ref = row.get('id', 'missing-id')
        def issue(message):
            errors.append({'creative_id': ref, 'issue': message})
        if ref == 'missing-id' or ref in ids:
            issue('Missing or duplicate creative ID')
        ids.add(ref)
        platform = row.get('platform')
        if platform not in {'linkedin', '6sense'}:
            issue('Unsupported platform')
        if row.get('review_state') != 'draft' or not row.get('buyer_group_id'):
            issue('New creative needs draft state and buyer-group ID')
        target = urlsplit(row.get('destination_url', ''))
        params = parse_qs(target.query, keep_blank_values=True)
        if base.scheme != 'https' or not base.netloc or (target.scheme, target.netloc, target.path.rstrip('/')) != (base.scheme, base.netloc, base.path.rstrip('/')):
            issue('Destination must use the supplied HTTPS campaign board')
        if any(key.casefold() in IDENTITY for key in params):
            issue('General paid-ad URL contains recipient identity')
        if params.get('utm_source') != [platform] or params.get('utm_medium') != [('paid_social' if platform == 'linkedin' else 'display')] or not params.get('utm_campaign') or not params.get('utm_content'):
            issue('Missing or inconsistent channel/creative attribution')
        for key, values in parse_qs(base.query, keep_blank_values=True).items():
            if params.get(key) != values:
                issue('Existing destination query values changed')
        if platform == 'linkedin':
            for field, limit in [('introductory_text', 150), ('headline', 70)]:
                value = row.get(field, '')
                if not isinstance(value, str) or not value.strip():
                    issue(f'Missing {field}')
                elif len(value) > limit:
                    warnings.append({'creative_id': ref, 'issue': f'{field} exceeds recommended {limit} characters'})
        name = row.get('image_file', '')
        path = (boundary / name).resolve()
        if not name or not path.is_relative_to(boundary) or path.suffix.lower() != '.png' or not path.is_file():
            issue('PNG file missing or outside handoff folder')
            continue
        data = path.read_bytes()
        if len(data) < 33 or data[:8] != b'\x89PNG\r\n\x1a\n' or data[12:16] != b'IHDR':
            issue('Invalid PNG header')
            continue
        size = struct.unpack('>II', data[16:24])
        if size != (row.get('width'), row.get('height')):
            issue('PNG dimensions differ from manifest')
        if platform == '6sense' and (size not in SIZES or not 1024 <= len(data) <= 150000):
            issue('6sense static dimensions or file weight outside checked limits')
        if platform == 'linkedin' and (size not in {(1200, 628), (1200, 1200)} or len(data) > 5000000):
            issue('Outside this handoff checker\'s LinkedIn export presets')
    return {'state': 'needs_revision' if errors else 'ready_for_creative_review', 'creative_count': len(manifest['creatives']),
            'errors': errors, 'warnings': warnings, 'launch_authorized': False,
            'limits': 'PNG headers and manifest checks only; inspect decoded images, claims, design and platform preview separately.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('manifest', type=Path)
    args = parser.parse_args()
    try:
        result = check_exports(json.loads(args.manifest.read_text()), args.manifest.parent)
    except (KeyError, TypeError, ValueError, OSError) as exc:
        parser.exit(2, f'Invalid handoff: {exc}\n')
    print(json.dumps(result, indent=2))
    raise SystemExit(1 if result['errors'] else 0)


if __name__ == '__main__':
    main()
