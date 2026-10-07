"""Converte apenas fotos reais selecionadas. Sem geração ou retoque de conteúdo."""
from pathlib import Path
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'research-assets'
OUTPUT = ROOT / 'assets' / 'images'
OUTPUT.mkdir(parents=True, exist_ok=True)

def photo(source, stem, widths):
    image = ImageOps.exif_transpose(Image.open(SOURCE / source)).convert('RGB')
    for width in widths:
        copy = image.copy()
        if image.width > width:
            copy = image.resize((width, round(width * image.height / image.width)), Image.Resampling.LANCZOS)
        filename = f'{stem}-{width}.webp' if len(widths) > 1 else f'{stem}.webp'
        copy.save(OUTPUT / filename, 'WEBP', quality=82, method=6)
        print(filename, copy.size, (OUTPUT / filename).stat().st_size)

photo('instagram-DZI3FZMPkNA-full.jpg', 'cozinha', [540, 810, 1080])
photo('instagram-DWB9FrTgP4M-full.jpg', 'drink', [450, 900])
photo('tripadvisor-carne-sol-macaxeira-cuscuz.jpg', 'macaxeira', [640, 1200])
photo('google-owner-fachada.jpg', 'fachada', [643])
photo('google-owner-salao-murais.jpg', 'salao', [635])
photo('logo-linktree-original.jpg', 'logo', [112])
logo = Image.open(SOURCE / 'logo-linktree-original.jpg').convert('RGB')
logo.resize((64, 64), Image.Resampling.LANCZOS).save(OUTPUT / 'favicon.png')
