"""Obtém as duas fontes de fontes oficiais; não é necessário na produção."""
import json
import re
from pathlib import Path
import requests

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / 'assets' / 'fonts'
TARGET.mkdir(parents=True, exist_ok=True)
headers = {'User-Agent': 'Mozilla/5.0 Chrome/120.0.0.0 Safari/537.36'}
families = [
    ('Fraunces', 'Fraunces:opsz,wght@9..144,400..700', 'fraunces-latin.woff2', 'fraunces'),
    ('DM Sans', 'DM+Sans:wght@400..700', 'dm-sans-latin.woff2', 'dmsans'),
]
sources = []
for name, family, filename, folder in families:
    css_url = f'https://fonts.googleapis.com/css2?family={family}&display=swap'
    response = requests.get(css_url, headers=headers, timeout=30)
    response.raise_for_status()
    latin = response.text.split('/* latin */')[-1]
    font_url = re.search(r'url\((https://[^)]+)\)', latin).group(1)
    response = requests.get(font_url, timeout=30)
    response.raise_for_status()
    (TARGET / filename).write_bytes(response.content)
    license_url = f'https://raw.githubusercontent.com/google/fonts/main/ofl/{folder}/OFL.txt'
    response = requests.get(license_url, timeout=30)
    response.raise_for_status()
    (TARGET / f'{folder}-OFL.txt').write_text(response.text, encoding='utf-8')
    sources.append({'family': name, 'file': filename, 'css': css_url, 'font': font_url, 'license': license_url})
    print(filename, (TARGET / filename).stat().st_size)
(TARGET / 'sources.json').write_text(json.dumps(sources, indent=2), encoding='utf-8')
