"""Verificação de referências, acessibilidade básica e precisão editorial."""
from pathlib import Path
from urllib.parse import urlsplit, unquote
from html.parser import HTMLParser
import re

ROOT = Path(__file__).resolve().parents[1]
errors = []

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.references, self.ids = [], set()
        self.h1_count = 0
        self.has_robots = False
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'html' and attrs.get('lang') != 'pt-BR':
            errors.append('Idioma incorreto')
        if tag == 'h1':
            self.h1_count += 1
        if 'id' in attrs:
            if attrs['id'] in self.ids:
                errors.append('ID duplicado: ' + attrs['id'])
            self.ids.add(attrs['id'])
        if tag == 'meta' and attrs.get('name') == 'robots':
            self.has_robots = attrs.get('content') == 'noindex, nofollow'
        if tag == 'img':
            if 'alt' not in attrs:
                errors.append('Imagem sem alt')
            if not all(attrs.get(x) for x in ('width','height')):
                errors.append('Imagem sem dimensões')
        for key in ('href', 'src'):
            if attrs.get(key):
                self.references.append(attrs[key])
        if attrs.get('srcset'):
            self.references += [v.strip().split()[0] for v in attrs['srcset'].split(',')]
        if attrs.get('target') == '_blank' and not {'noopener','noreferrer'}.issubset(set(attrs.get('rel','').split())):
            errors.append('Link externo sem rel seguro')

total = 0
for file in [ROOT/'index.html', ROOT/'creditos.html']:
    source = file.read_text(encoding='utf-8')
    parsed = Page()
    parsed.feed(source)
    if parsed.h1_count != 1:
        errors.append(f'{file.name}: esperado um h1')
    if not parsed.has_robots:
        errors.append(f'{file.name}: falta noindex, nofollow')
    for url in parsed.references:
        total += 1
        parts = urlsplit(url)
        if parts.scheme or url.startswith('//'):
            continue
        if url.startswith('/'):
            errors.append('Caminho absoluto incompatível com Pages: ' + url)
        if parts.path and not (file.parent / unquote(parts.path)).exists():
            errors.append(f'{file.name}: referência ausente {url}')
        if not parts.path and parts.fragment not in parsed.ids:
            errors.append(f'{file.name}: âncora ausente {url}')
    forbidden = ['uma verdadeira viagem de sabores','experiência única','sabores que contam histórias','tradição e inovação','feito com amor','o melhor do Nordeste em cada garfada','—']
    for expression in forbidden:
        if expression.lower() in source.lower():
            errors.append(f'{file.name}: expressão proibida {expression}')
    if re.search(r'R\$\s*\d', source):
        errors.append(f'{file.name}: preço numérico não autorizado')

css = ROOT/'assets/css/site.css'
for groups in re.findall(r'''url\((?:'([^']*)'|"([^"]*)"|([^)]*))\)''', css.read_text(encoding='utf-8')):
    url = next((value for value in groups if value), '')
    if not url.startswith('data:') and not (css.parent/url).exists():
        errors.append('CSS: asset ausente ' + url)
for filename in ['README.md','docs/RESEARCH.md','docs/ASSET_SOURCES.md','docs/QA_REPORT.md','CREATIVE_DIRECTION.md','SITE_STRATEGY.md','SELF_CRITIQUE.md']:
    if not (ROOT/filename).exists():
        errors.append('Documento ausente: ' + filename)
if errors:
    raise SystemExit('\n'.join(errors))
print(f'PASS: {total} referências, âncoras, imagens, fontes, noindex e controles editoriais.')
