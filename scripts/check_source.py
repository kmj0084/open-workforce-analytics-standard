"""Small dependency-free checks for the deliberately simple front matter convention."""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
errors = []
ids = set()
for section in ('standards', 'research', 'essays'):
    for path in (root / section).rglob('*.qmd'):
        text = path.read_text(encoding='utf-8')
        front = text.split('---', 2)[1] if text.startswith('---\n') else ''
        meta = dict(re.findall(r'^([\w-]+):\s*(.+)$', front, re.M))
        if 'content-type' not in meta:
            continue
        required = ['title', 'description', 'date', 'date-modified', 'categories', 'draft']
        if meta['content-type'] == 'metric':
            required += ['metric-id', 'domain', 'metric-type', 'status', 'version']
            ident = meta.get('metric-id')
            if ident in ids:
                errors.append(f'{path.relative_to(root)}: duplicate metric ID {ident}')
            ids.add(ident)
            if meta.get('status') not in ['Draft', 'Review', 'Recommended', 'Deprecated']:
                errors.append(f'{path.relative_to(root)}: invalid metric status')
        for key in required:
            if key not in meta:
                errors.append(f'{path.relative_to(root)}: missing {key}')
        if meta.get('draft') not in ['true', 'false']:
            errors.append(f'{path.relative_to(root)}: draft must be true or false')
if errors:
    raise SystemExit('\n'.join(errors))
print('Source metadata checks passed.')
