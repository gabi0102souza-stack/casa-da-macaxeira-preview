"""Confere resposta HTTPS e igualdade dos arquivos de produção no Pages."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://gabi0102souza-stack.github.io/casa-da-macaxeira-preview/'
paths = [ROOT / name for name in ('index.html', 'creditos.html', 'robots.txt')]
paths += sorted((ROOT / 'assets').rglob('*'))
paths = [path for path in paths if path.is_file()]

def check(path):
    name = path.relative_to(ROOT).as_posix()
    url = BASE + ('' if name == 'index.html' else name)
    result = {'file': name, 'url': url}
    try:
        with urlopen(Request(url, headers={'User-Agent': 'CasaProposalQA/1.0'}), timeout=30) as response:
            data = response.read()
            result.update(status=response.status, content_type=response.headers.get('Content-Type'), bytes=len(data))
        local = path.read_bytes()
        same = data == local
        # Git can normalize text line endings while preserving mixed files.
        if not same and path.suffix in ('.html', '.css', '.js', '.txt', '.json'):
            same = data.replace(b'\r\n', b'\n') == local.replace(b'\r\n', b'\n')
        result.update(sha256=sha256(data).hexdigest(), matches_local=same)
    except Exception as error:
        result.update(status='ERROR', error=str(error), matches_local=False)
    return result

with ThreadPoolExecutor(max_workers=4) as pool:
    checks = list(pool.map(check, paths))
report = {'checked_at_utc': datetime.now(timezone.utc).isoformat(), 'base_url': BASE,
          'pass': all(item['status'] == 200 and item['matches_local'] for item in checks), 'files': checks}
if report['pass']:
    (ROOT / 'docs/qa/public-http.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'pass': report['pass'], 'checked': len(checks), 'failures': [item for item in checks if not item['matches_local']]}, ensure_ascii=False))
raise SystemExit(0 if report['pass'] else 1)
