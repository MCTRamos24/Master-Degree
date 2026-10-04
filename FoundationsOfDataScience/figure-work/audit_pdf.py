"""Render every PDF page and create numbered sheets for visual review."""
from pathlib import Path
import subprocess
from PIL import Image, ImageOps, ImageDraw
from pypdf import PdfReader

root = Path(__file__).resolve().parent.parent
out = root / 'figure-work' / 'polished-pages'
out.mkdir(exist_ok=True)
pdf = root / 'FoundationsOfDataScience.pdf'
reader = PdfReader(pdf)
text = '\n'.join(page.extract_text() or '' for page in reader.pages)
(out / 'document-text.txt').write_text(text, encoding='utf-8')
subprocess.run(['pdftoppm', '-r', '110', '-png', str(pdf), str(out / 'page')],check=True)
files = sorted(out.glob('page-*.png'))
for offset in range(0,len(files),4):
    sheet = Image.new('RGB',(1100,1610),'#dddddd')
    draw = ImageDraw.Draw(sheet)
    for j,p in enumerate(files[offset:offset+4]):
        tile = ImageOps.contain(Image.open(p).convert('RGB'),(540,770))
        x,y = (j%2)*550,(j//2)*805
        sheet.paste(tile,(x,y+25))
        draw.text((x+12,y+6),f'PDF page {offset+j+1}',fill='black')
    sheet.save(out / f'sheet-{offset//4+1:02}.png')
print(f'Rendered {len(reader.pages)} pages; {len(files)} page images.')
