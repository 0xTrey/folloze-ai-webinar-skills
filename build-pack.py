#!/usr/bin/env python3
"""Build portable customer skill downloads from an explicit file allowlist."""
import hashlib
import json
import re
import tempfile
from pathlib import Path
from urllib.parse import unquote, urlsplit
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parent
BASE = ('SKILL.md', 'QUICKSTART.md', 'agents/openai.yaml',
        'references/tool-map-use.md', 'scripts/check_tool_budget.py')
FOLLOW_UP = BASE + ('references/context-and-evidence.md', 'references/output-template.md')
SKILLS = {
    'tools-data-setup': BASE + ('references/tool-map-template.md', 'references/enrichment-and-limits.md'),
    'company-brain-builder': BASE + ('references/company-brain-template.md', 'references/document-requests.md', 'references/storage-and-use.md'),
    'campaign-segmentation': FOLLOW_UP,
    'account-brief-builder': FOLLOW_UP,
    'buyer-group-mapper': FOLLOW_UP,
    'buyer-group-ad-creative': FOLLOW_UP,
    'buyer-group-email-copy': FOLLOW_UP,
    'campaign-workspace': ('SKILL.md', 'QUICKSTART.md', 'agents/openai.yaml',
        'references/runtime.md', 'references/result-contract.md',
        'assets/campaign-workspace.html', 'assets/OpenSans-OFL.txt',
        'assets/THIRD_PARTY_NOTICES.txt'),
}
SKILL_FILES = {f'skills/{name}/{file}' for name, files in SKILLS.items() for file in files}
ARCHIVES = [f'{name}.zip' for name in SKILLS] + ['folloze-ai-webinar-skills.zip']
ALLOWED = SKILL_FILES | {'README.md', 'START-HERE.md', '.gitignore', '.gitattributes', 'build-pack.py', 'downloads/manifest.json'} | {f'downloads/{name}' for name in ARCHIVES}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def inventory(root):
    found = set()
    for file in root.rglob('*'):
        relative = file.relative_to(root)
        if '.git' in relative.parts or '__pycache__' in relative.parts or file.name == '.DS_Store':
            continue
        if file.is_symlink():
            raise ValueError(f'Symlink is not allowed: {relative}')
        if file.is_file():
            found.add(relative.as_posix())
    return found


def links(file, boundary):
    body = file.read_text()
    count = 0
    for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)', body):
        target = target.strip('<>')
        if urlsplit(target).scheme or target.startswith('#'):
            continue
        resolved = (file.parent / unquote(urlsplit(target).path)).resolve()
        if not resolved.is_relative_to(boundary.resolve()) or not resolved.is_file():
            raise ValueError(f'Broken or escaping reference: {file.relative_to(boundary)} -> {target}')
        count += 1
    return count


def audit_attendee_file(file):
    text = file.read_text()
    # Customer files are templates and instructions, never working campaign data.
    forbidden = r'/Users/|/home/|(?<![A-Za-z0-9_])[A-Za-z]:\\|github_pat_[A-Za-z0-9_]+|gh[pousr]_[A-Za-z0-9]+|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----'
    if re.search(forbidden, text, re.I):
        raise ValueError(f'Private or campaign-specific content: {file.relative_to(ROOT)}')
    if file.suffix in {'.md', '.yaml', '.py'} and '\u2014' in text:
        raise ValueError(f'Use plain punctuation: {file.relative_to(ROOT)}')


def archive(name, members):
    destination = ROOT / 'downloads' / name
    rows = []
    with ZipFile(destination, 'w', compression=ZIP_DEFLATED) as bundle:
        for member, data in sorted(members.items()):
            info = ZipInfo(member, date_time=(2026, 10, 14, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            bundle.writestr(info, data)
            rows.append({'path': member, 'bytes': len(data), 'sha256': sha(data)})
    with ZipFile(destination) as bundle:
        if bundle.testzip() or set(bundle.namelist()) != set(members):
            raise ValueError(f'Archive integrity failed: {name}')
        for member, expected in members.items():
            if bundle.read(member) != expected:
                raise ValueError(f'Archive bytes differ: {member}')
        with tempfile.TemporaryDirectory(prefix='customer-skills-check-') as scratch:
            bundle.extractall(scratch)
            extracted = Path(scratch)
            for member in members:
                if member.endswith('.md'):
                    links(extracted / member, extracted)
    return {'name': name, 'bytes': destination.stat().st_size,
            'sha256': sha(destination.read_bytes()), 'fileCount': len(rows), 'files': rows}


def main():
    unexpected = inventory(ROOT) - ALLOWED
    if unexpected:
        raise ValueError(f'Unexpected files outside public allowlist: {sorted(unexpected)}')
    expected_skill_names = set(SKILLS)
    if {p.name for p in (ROOT / 'skills').iterdir()} != expected_skill_names:
        raise ValueError('Skill folders do not match the public allowlist')
    for name, files in SKILLS.items():
        folder = ROOT / 'skills' / name
        if inventory(folder) != set(files):
            raise ValueError(f'Unexpected or missing resources: {name}')
    for relative in sorted(SKILL_FILES | {'START-HERE.md'}):
        file = ROOT / relative
        audit_attendee_file(file)
        if file.suffix == '.md':
            links(file, ROOT / 'skills' / file.relative_to(ROOT / 'skills').parts[0] if relative.startswith('skills/') else ROOT)
    for resource in ('references/tool-map-use.md', 'scripts/check_tool_budget.py'):
        copies = {(ROOT / 'skills' / name / resource).read_bytes() for name in SKILLS if name != 'campaign-workspace'}
        if len(copies) != 1:
            raise ValueError(f'Shared tool-map resources differ: {resource}')
    (ROOT / 'downloads').mkdir(exist_ok=True)
    archives = []
    for name, files in SKILLS.items():
        archives.append(archive(f'{name}.zip', {f'{name}/{file}': (ROOT / 'skills' / name / file).read_bytes() for file in files}))
    full = {f'folloze-ai-webinar-skills/{name}': (ROOT / name).read_bytes() for name in SKILL_FILES | {'START-HERE.md'}}
    archives.append(archive('folloze-ai-webinar-skills.zip', full))
    manifest = {'version': '0.1.0', 'skillCount': len(SKILLS), 'skillFileCount': len(SKILL_FILES),
                'checks': ['explicit file allowlist', 'portable paths', 'relative references', 'archive CRC', 'source byte parity', 'fresh extraction'],
                'artifacts': archives}
    (ROOT / 'downloads/manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    if inventory(ROOT) != ALLOWED:
        raise ValueError('Public repository inventory differs from the allowlist')
    audit_attendee_file(ROOT / 'README.md')
    links(ROOT / 'README.md', ROOT)
    print(json.dumps({'skills': len(SKILLS), 'skillFiles': len(SKILL_FILES), 'downloads': len(archives),
                      'fullPackFiles': archives[-1]['fileCount'], 'allChecks': 'pass'}, indent=2))


if __name__ == '__main__':
    main()
