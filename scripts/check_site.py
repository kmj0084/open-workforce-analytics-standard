"""Check rendered local links, search coverage, and the starter draft fixture."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import json

root = Path(__file__).resolve().parents[1] / '_site'
errors = []
class Links(HTMLParser):
    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key not in ('href', 'src') or not value:
                continue
            url = urlsplit(value)
            if url.scheme or url.netloc or not url.path:
                continue
            target = root / unquote(url.path).lstrip('/') if url.path.startswith('/') else self.path.parent / unquote(url.path)
            if not target.exists():
                errors.append(f'{self.path.relative_to(root)}: missing target {value}')

pages = list(root.rglob('*.html'))
assert pages, 'No rendered HTML found; run quarto render first.'
for page in pages:
    parser = Links()
    parser.path = page
    parser.feed(page.read_text(encoding='utf-8'))
for file in root.rglob('*'):
    if file.is_file() and file.suffix in ('.html', '.json', '.xml'):
        if 'OWAS-DRAFT-SENTINEL-7C92' in file.read_text(encoding='utf-8'):
            errors.append(f'Draft body leaked into {file.relative_to(root)}')
search = json.loads((root / 'search.json').read_text(encoding='utf-8'))
search_text = json.dumps(search)
for title in ['Point-in-time headcount', 'Record both the effective date', 'Start with what a number counts']:
    if title not in search_text:
        errors.append(f'Search missing starter content: {title}')
for forbidden in ['unpublished-example', 'templates/']:
    if forbidden in search_text:
        errors.append(f'Search includes excluded path: {forbidden}')
for landing in ['research/index.html', 'standards/index.html', 'essays/index.html']:
    if 'unpublished-example' in (root / landing).read_text(encoding='utf-8'):
        errors.append(f'Draft linked in {landing}')
if (root / 'templates').exists():
    errors.append('Templates were copied into the published site.')
if errors:
    raise SystemExit('\n'.join(errors))
print(f'Render checks passed: {len(pages)} HTML pages, local link targets, search coverage, draft exclusion.')
