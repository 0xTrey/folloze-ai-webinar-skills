#!/usr/bin/env python3
"""Build portable customer skill downloads from an explicit file allowlist."""
import hashlib
import html
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
    'account-list-builder': FOLLOW_UP,
    'campaign-segmentation': FOLLOW_UP,
    'account-brief-builder': FOLLOW_UP,
    'buyer-group-mapper': FOLLOW_UP,
    'buyer-group-ad-creative': FOLLOW_UP + ('references/platform-formats.md', 'scripts/check_ad_exports.py'),
    'buyer-group-email-copy': FOLLOW_UP + ('references/messaging-framework.md', 'references/delivery-handoffs.md', 'scripts/check_email_batch.py'),
    'follow-up-measurement': FOLLOW_UP,
    'campaign-workspace': ('SKILL.md', 'QUICKSTART.md', 'agents/openai.yaml',
        'references/runtime.md', 'references/result-contract.md',
        'assets/campaign-workspace.html', 'assets/OpenSans-OFL.txt',
        'assets/THIRD_PARTY_NOTICES.txt'),
}
SKILL_FILES = {f'skills/{name}/{file}' for name, files in SKILLS.items() for file in files}
GUIDES = {'CUSTOMER-GUIDE.md', 'START-HERE.md', 'CLAUDE-REHEARSAL.md', 'CAMPAIGN-PROMPTS.md', 'CAMPAIGN-PROMPTS.html'}
ARCHIVES = [f'{name}.zip' for name in SKILLS] + ['campaign-prompts.zip', 'claude-campaign-kit.zip', 'claude-rehearsal-kit.zip', 'folloze-ai-webinar-skills.zip']
ALLOWED = SKILL_FILES | GUIDES | {'README.md', '.gitignore', '.gitattributes', 'build-pack.py', 'downloads/manifest.json'} | {f'downloads/{name}' for name in ARCHIVES}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def build_embedded_skills():
    """Refresh the standalone app's actual instructions from this release."""
    stages = {
        'company-brain-builder': ('Company Brain Builder', 'brain'),
        'tools-data-setup': ('Tools & Data Setup', 'tools'),
        'account-list-builder': ('Build the Right Account List', 'accounts'),
        'campaign-segmentation': ('Campaign Segmentation', 'segments'),
        'account-brief-builder': ('Account Brief Builder', 'briefs'),
        'buyer-group-mapper': ('Buyer Group Mapper', 'buyers'),
        'buyer-group-ad-creative': ('Buyer Group Ad Creative', 'messages'),
        'buyer-group-email-copy': ('Buyer Group Email Copy', 'messages'),
        'follow-up-measurement': ('Engagement & Follow-up', 'followup'),
    }
    if set(stages) != set(SKILLS) - {'campaign-workspace'}:
        raise ValueError('Embedded skill stage mapping differs from the pack')
    bundled = []
    for name, (title, step) in stages.items():
        folder = ROOT / 'skills' / name
        entry = (folder / 'SKILL.md').read_text()
        description = re.search(r'^description: (.+)$', entry, re.M)
        if not description:
            raise ValueError(f'Missing skill description: {name}')
        description = description[1].strip()
        if description.startswith('"'):
            description = json.loads(description)
        resources = {}
        for relative in SKILLS[name]:
            data = (folder / relative).read_bytes()
            resources[relative] = {'text': data.decode('utf-8'), 'sha256': sha(data)}
        bundled.append({'name': name, 'title': title, 'step': step,
                        'description': description, 'files': resources})
    payload = json.dumps({'version': 2, 'source': 'Folloze customer campaign skills',
                          'skills': bundled}, ensure_ascii=True, separators=(',', ':'))
    payload = payload.replace('<', '\\u003c').replace('>', '\\u003e')
    app = ROOT / 'skills/campaign-workspace/assets/campaign-workspace.html'
    before = app.read_text()
    start = '<script>(()=>{var co='
    end = ';var ht=co.skills;'
    if before.count(start) != 1 or before.count(end) != 1:
        raise ValueError('Standalone app bundle boundary is ambiguous')
    left = before.index(start) + len(start)
    right = before.index(end, left)
    output = before[:left] + payload + before[right:]
    library_copy = r'(?:Seven webinar|[0-9]+ campaign) skills are included with their references\.'
    output, count = re.subn(library_copy, f'{len(bundled)} campaign skills are included with their references.', output)
    if count != 1:
        raise ValueError('Standalone skill library count label is ambiguous')
    app.write_text(output)
    return len(bundled)


def build_prompt_browser():
    """Derive the offline prompt browser from the canonical Markdown cards."""
    source = (ROOT / 'CAMPAIGN-PROMPTS.md').read_text()
    records = re.findall(r'^### (\d+)\. ([^\n]+)\n(.*?)(?=^### |^## Keep the work connected|\Z)', source, re.M | re.S)
    if [int(n) for n, _, _ in records] != list(range(1, 21)):
        raise ValueError('Expected exactly 20 sequential prompt cards')
    cards, stages = [], []

    def inline(value):
        return re.sub(r'\[([^\]]+)\]\((https://[^)]+)\)',
                      r'<a href="\2" target="_blank" rel="noopener">\1</a>', html.escape(value))

    for number, title, body in records:
        fields = {}
        for key in ('Stage', 'Skill', 'Bring', 'Get'):
            match = re.search(r'^\*\*' + key + r':\*\* (.+)$', body, re.M)
            if not match:
                raise ValueError(f'Missing {key} on prompt {number}')
            fields[key] = match[1]
        blocks = re.findall(r'```text\n(.*?)\n```', body, re.S)
        if len(blocks) != 1 or not blocks[0].strip():
            raise ValueError(f'Expected one usable prompt block on card {number}')
        if fields['Stage'] not in stages:
            stages.append(fields['Stage'])
        cards.append(f'''<details class="prompt-card" id="prompt-{number}" data-stage="{html.escape(fields['Stage'], quote=True)}">
<summary><b>{number}</b><span>{html.escape(title)}</span><small>{html.escape(fields['Stage'])}</small></summary>
<div class="card-body"><p class="skill"><strong>Skill</strong> {inline(fields['Skill'])}</p>
<dl><div><dt>Bring</dt><dd>{html.escape(fields['Bring'])}</dd></div><div><dt>Get</dt><dd>{html.escape(fields['Get'])}</dd></div></dl>
<button type="button" class="copy" data-number="{number}" aria-label="Copy prompt {number}">Copy prompt</button>
<pre tabindex="0">{html.escape(blocks[0])}</pre></div></details>''')
    options = ''.join(f'<option value="{html.escape(stage, quote=True)}">{html.escape(stage)}</option>' for stage in stages)
    template = '''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="prompt-source-sha256" content="__SOURCE_HASH__"><title>20 campaign prompts | Folloze</title>
<style>
:root{font-family:system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;color:#071428;background:#f3f9fd;font-synthesis:none}*{box-sizing:border-box}body{margin:0}main{max-width:1080px;margin:auto;padding:48px 28px 60px}h1{font-size:clamp(29px,4vw,43px);line-height:1.12;letter-spacing:-1.2px;margin:0 0 22px}p{line-height:1.6}a{color:#005aca}header>p{max-width:800px;color:#2c3d59}.links{display:flex;gap:10px 24px;flex-wrap:wrap;margin:24px 0;font-size:14px}.toolbar{display:grid;grid-template-columns:1fr 1fr auto;gap:14px;align-items:end;padding:20px;background:white;border:1px solid #cce1f3;border-radius:6px;margin:28px 0 16px}.toolbar label{font-size:12px;font-weight:700;display:flex;gap:8px;flex-direction:column}input,select,button{font:inherit;border:1px solid #b8d2e8;border-radius:4px;color:inherit;background:white}input,select{padding:11px;width:100%;min-width:0;font-size:14px}button{cursor:pointer;padding:11px 16px;font-size:13px;font-weight:650}button:hover{border-color:#0077ff}button:focus-visible,summary:focus-visible,a:focus-visible,input:focus-visible,select:focus-visible,pre:focus-visible{outline:3px solid #0077ff;outline-offset:3px}#result-count,#copy-status{font-size:12px;color:#52627a;min-height:18px}#copy-status{color:#005aca}.prompt-card{border:1px solid #cce1f3;background:white;border-radius:6px;margin:11px 0}.prompt-card[hidden]{display:none}summary{display:grid;grid-template-columns:30px 1fr auto;gap:12px;align-items:center;padding:19px 20px;cursor:pointer;list-style:none}summary::-webkit-details-marker{display:none}summary>b{color:#005aca;font-size:13px}summary>span{font-size:16px;font-weight:700}summary>small{font-size:11px;max-width:160px;color:#52627a;text-align:right}.prompt-card[open]{border-color:#0077ff}.prompt-card[open] summary{border-bottom:1px solid #d8ecfa}.card-body{padding:22px}.skill{font-size:13px;margin:0 0 18px}.skill strong{margin-right:9px}dl{margin:0 0 22px;font-size:13px}dl>div{display:grid;grid-template-columns:55px 1fr;gap:12px;margin:10px 0}dt{font-weight:700}dd{margin:0;line-height:1.6}.copy{color:white;background:#0077ff;border-color:#0077ff}pre{white-space:pre-wrap;overflow-wrap:anywhere;font:14px/1.75 system-ui,-apple-system,sans-serif;background:#f3f9fd;border:1px solid #d8ecfa;padding:20px;border-radius:4px;margin:17px 0 0}footer{font-size:12px;color:#52627a;border-top:1px solid #cce1f3;margin-top:30px;padding-top:20px}#empty{padding:24px;background:white;border:1px solid #cce1f3;border-radius:6px}@media(max-width:650px){main{padding:30px 16px}.toolbar{grid-template-columns:1fr}.toolbar button{justify-self:start}summary{grid-template-columns:23px 1fr;padding:17px 14px}summary>small{grid-column:2;text-align:left;max-width:none}.card-body{padding:17px}pre{padding:16px}.links{gap:12px 18px}}@media print{body{background:white}main{max-width:none;padding:0}.toolbar,.copy,.links,#copy-status{display:none}.prompt-card{break-inside:avoid}pre{background:white}}
</style></head><body><main>
<header><h1>20 prompts for your next campaign.</h1><p>From company context to a useful sales conversation. Choose a prompt, attach its inputs and make something you can review. Each card can start a separate chat.</p>
<nav class="links" aria-label="Downloads"><a href="CAMPAIGN-PROMPTS.md">Markdown handout</a><a href="https://github.com/0xTrey/folloze-ai-webinar-skills">Skills and downloads</a></nav></header>
<section class="toolbar" aria-label="Find a prompt"><label for="search">Search prompts<input id="search" type="search" placeholder="Email, account brief, engagement..."></label><label for="stage">Campaign section<select id="stage"><option value="all">All sections</option>__OPTIONS__</select></label><button type="button" id="expand">Expand all</button></section>
<p id="result-count" aria-live="polite">20 prompts</p><p id="copy-status" role="status"></p>
<section id="cards" aria-label="Campaign prompts">__CARDS__</section><p id="empty" hidden>No prompts match. Try another search or section.</p>
<footer>Folloze AI webinar leave-behind. Replace the braces with your values. Included skills are linked on each card; workflow prompts use your files and available tools. Keep private inputs in your approved workspace. New copy, creative and pages stay drafts. Connections do not authorize spending or launch.</footer>
</main><script>
const cards=[...document.querySelectorAll('.prompt-card')],search=document.getElementById('search'),stage=document.getElementById('stage'),status=document.getElementById('copy-status');
function filter(){const query=search.value.trim().toLowerCase();let count=0;for(const card of cards){card.hidden=(stage.value!=='all'&&card.dataset.stage!==stage.value)||(query&&!card.textContent.toLowerCase().includes(query));if(!card.hidden)count++;}document.getElementById('result-count').textContent=count+' of 20 prompts';document.getElementById('empty').hidden=!!count;}
search.addEventListener('input',filter);stage.addEventListener('change',filter);
document.getElementById('expand').addEventListener('click',event=>{const visible=cards.filter(card=>!card.hidden),open=visible.some(card=>!card.open);for(const card of visible)card.open=open;event.currentTarget.textContent=open?'Collapse all':'Expand all';});
for(const button of document.querySelectorAll('.copy'))button.addEventListener('click',async()=>{const pre=button.closest('details').querySelector('pre');try{await navigator.clipboard.writeText(pre.textContent);button.textContent='Copied';status.textContent='Prompt '+button.dataset.number+' copied.';}catch{const selection=window.getSelection(),range=document.createRange();range.selectNodeContents(pre);selection.removeAllRanges();selection.addRange(range);pre.focus();status.textContent='Prompt '+button.dataset.number+' selected. Press Command+C or Ctrl+C to copy.';}});
if(location.hash.startsWith('#prompt-')){const card=document.getElementById(location.hash.slice(1));if(card){card.open=true;card.scrollIntoView();}}
window.addEventListener('beforeprint',()=>{for(const card of cards)card.open=true;});
</script></body></html>'''
    output = template.replace('__OPTIONS__', options).replace('__CARDS__', '\n'.join(cards)).replace('__SOURCE_HASH__', sha(source.encode()))
    (ROOT / 'CAMPAIGN-PROMPTS.html').write_text(output)
    return len(cards)


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
    prompt_count = build_prompt_browser()
    embedded_count = build_embedded_skills()
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
    for relative in sorted(SKILL_FILES | GUIDES):
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
    prompt_files = ('CAMPAIGN-PROMPTS.md', 'CAMPAIGN-PROMPTS.html')
    archives.append(archive('campaign-prompts.zip', {f'campaign-prompts/{name}': (ROOT / name).read_bytes() for name in prompt_files}))
    claude_kit = {f'claude-campaign-kit/skill-zips/{name}.zip': (ROOT / 'downloads' / f'{name}.zip').read_bytes() for name in SKILLS}
    for name in ('CUSTOMER-GUIDE.md',) + prompt_files:
        claude_kit[f'claude-campaign-kit/{name}'] = (ROOT / name).read_bytes()
    for name in ('campaign-workspace.html', 'OpenSans-OFL.txt', 'THIRD_PARTY_NOTICES.txt'):
        claude_kit[f'claude-campaign-kit/{name}'] = (ROOT / 'skills/campaign-workspace/assets' / name).read_bytes()
    archives.append(archive('claude-campaign-kit.zip', claude_kit))
    # Retain the old download URL with the same customer-facing contents.
    archives.append(archive('claude-rehearsal-kit.zip', claude_kit))
    full = {f'folloze-ai-webinar-skills/{name}': (ROOT / name).read_bytes() for name in SKILL_FILES | GUIDES}
    archives.append(archive('folloze-ai-webinar-skills.zip', full))
    manifest = {'version': '0.3.2', 'skillCount': len(SKILLS), 'embeddedSkillCount': embedded_count, 'skillFileCount': len(SKILL_FILES), 'promptCount': prompt_count,
                'checks': ['customer onboarding content', 'explicit file allowlist', 'portable paths', 'relative references', 'archive CRC', 'source byte parity', 'fresh extraction'],
                'artifacts': archives}
    (ROOT / 'downloads/manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    if inventory(ROOT) != ALLOWED:
        raise ValueError('Public repository inventory differs from the allowlist')
    for name in ('README.md',) + tuple(GUIDES):
        if re.search(r'rehears(?:e|al|ing)|presenter guide', (ROOT / name).read_text(), re.I):
            raise ValueError(f'Internal presentation content in customer file: {name}')
    audit_attendee_file(ROOT / 'README.md')
    links(ROOT / 'README.md', ROOT)
    print(json.dumps({'skills': len(SKILLS), 'skillFiles': len(SKILL_FILES), 'downloads': len(archives),
                      'fullPackFiles': archives[-1]['fileCount'], 'allChecks': 'pass'}, indent=2))


if __name__ == '__main__':
    main()
