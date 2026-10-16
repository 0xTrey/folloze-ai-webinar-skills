#!/usr/bin/env python3
"""Read-only structural and same-company duplicate checks for email drafts."""
import argparse
from collections import defaultdict
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit


def normal(value):
    return re.sub(r'[^\w]+', ' ', str(value).casefold(), flags=re.UNICODE).strip()


def check_batch(batch):
    if not isinstance(batch, dict):
        raise ValueError('Batch must be a JSON object')
    errors, warnings = [], []
    drafts = batch.get('drafts', [])
    if not isinstance(drafts, list) or not drafts:
        return {'state': 'needs_revision', 'draft_count': 0, 'errors': [{'draft_id': None, 'issue': 'No draft rows'}], 'warnings': []}
    pitches = {p['id']: p for p in batch.get('pitches', [])}
    destination = urlsplit(batch.get('destination_url', ''))
    board_path = destination.path.rstrip('/')
    verified_items = batch.get('verified_board_item_urls') or []
    if not isinstance(verified_items, list) or not all(isinstance(u, str) for u in verified_items):
        raise ValueError('verified_board_item_urls must be a list of clean item URLs')
    allowed_paths = {board_path}
    for url in verified_items:
        item = urlsplit(url)
        path = item.path.rstrip('/')
        if (item.scheme == destination.scheme == 'https' and item.netloc == destination.netloc
                and path.startswith(board_path + '/items/') and not item.query and not item.fragment
                and not {'.', '..'}.intersection(unquote(path).split('/'))):
            allowed_paths.add(path)
    seen = defaultdict(dict)
    prior = batch.get('prior_messages', [])
    if not isinstance(prior, list):
        raise ValueError('prior_messages must be a list')
    for i, row in enumerate(prior + drafts):
        if not isinstance(row, dict):
            raise ValueError('Each message must be a JSON object')
        is_new = i >= len(prior)
        ref = row.get('id', f'row-{i+1}')
        def issue(message):
            errors.append({'draft_id': ref, 'issue': message})
        campaign = row.get('campaign_id', batch.get('campaign_id'))
        company = row.get('company_key')
        touch = row.get('touch', 1)
        pitch_text = row.get('pitch_text', row.get('pitch', ''))
        if is_new:
            for field in ('subject', 'opening', 'bridge', 'cta', 'resource_id'):
                if not isinstance(row.get(field), str) or not row[field].strip():
                    issue(f'Missing {field}')
            if not campaign or not company or not isinstance(touch, int) or isinstance(touch, bool) or touch < 1:
                issue('Missing or invalid company/campaign/touch scope')
            if normal(row.get('review_state', '')) != 'draft':
                issue('New messages must remain draft')
            pitch = pitches.get(row.get('pitch_id'))
            if not pitch or pitch.get('text') != pitch_text:
                issue('Pitch differs from the supplied library')
            elif pitch.get('approval') != 'approved':
                warnings.append({'draft_id': ref, 'issue': 'Pitch wording is not approved'})
            target = urlsplit(row.get('cta_url', row.get('board_url', row.get('url', ''))))
            if (destination.scheme != 'https' or not destination.netloc or
                target.scheme != destination.scheme or target.netloc != destination.netloc or
                target.path.rstrip('/') not in allowed_paths):
                issue('CTA must use the supplied campaign board or an explicitly verified item on it')
            visible = '\n'.join(str(row.get(f, '')) for f in ('subject', 'opening', 'bridge', 'cta'))
            subject = row.get('subject', '')
            if isinstance(subject, str) and (not 2 <= len(subject.split()) <= 8 or len(subject) > 70 or re.search(r'[\r\n]', subject)):
                issue('Subject must have 2-8 words, at most 70 characters and no newlines')
            if re.search(r'\{\{|\[first.?name\]', visible, re.I):
                issue('Unresolved copy placeholder')
            if re.search(r'https?://', visible):
                issue('Keep the URL in board_url, outside the visible copy sections')
            body = '\n'.join((str(row.get('body', visible + '\n' + pitch_text)), str(row.get('signature', ''))))
            if re.search(r'\{\{|\[first.?name\]', body, re.I):
                issue('Unresolved rendered-body placeholder')
            if batch.get('footer_policy') == 'signature_only' and re.search(
                    r'Advertisement from|Not relevant\?|reply no|unsubscribe here|Folloze, Inc\.', body, re.I):
                issue('Remove the appended footer')
        group = (normal(company), str(campaign), touch)
        copy = ' '.join((row.get('opening', ''), row.get('bridge', ''), pitch_text, row.get('cta', '')))
        for field, value in (('subject', row.get('subject')), ('opening', row.get('opening')), ('body', copy)):
            normalized = normal(value or '')
            if not normalized:
                continue
            key = (field, normalized)
            if is_new and key in seen[group]:
                issue(f'Duplicate {field} within company/campaign/touch, including supplied history')
            seen[group][key] = ref
    return {'state': 'needs_revision' if errors else 'ready_for_copy_review', 'draft_count': len(drafts),
            'errors': errors, 'warnings': warnings, 'sending_authorized': False,
            'limits': 'Structural checks and supplied exact-duplicate history only; factual and semantic review remain.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('batch', type=Path)
    args = parser.parse_args()
    try:
        result = check_batch(json.loads(args.batch.read_text()))
    except (KeyError, TypeError, ValueError) as exc:
        parser.exit(2, f'Invalid batch: {exc}\n')
    print(json.dumps(result, indent=2))
    raise SystemExit(1 if result['errors'] else 0)


if __name__ == '__main__':
    main()
