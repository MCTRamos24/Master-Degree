"""Render every notes page and generate readable contact sheets for inspection."""
from pathlib import Path
import subprocess
from PIL import Image, ImageDraw, ImageFont

out=Path('out/refinement/pages')
out.mkdir(exist_ok=True)
for old in out.glob('page-*.png'):
    old.unlink()
for old in out.glob('contact-*.png'):
    old.unlink()
subprocess.run(['pdftoppm','-r','110','-png','out/ComputerVision.pdf',str(out/'page')],check=True,capture_output=True)
pages=sorted(out.glob('page-*.png'))
font=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',18)
for start in range(0,len(pages),12):
    sheet=Image.new('RGB',(1560,1710),'#dddddd')
    draw=ImageDraw.Draw(sheet)
    for j,f in enumerate(pages[start:start+12]):
        im=Image.open(f).convert('RGB'); im.thumbnail((375,525))
        x=(j%4)*390+7; y=(j//4)*570+30
        sheet.paste(im,(x,y))
        draw.text((x,y-25),f'PDF page {start+j+1}',font=font,fill='black')
    sheet.save(out/f'contact-{start//12+1}.png')
master=Image.new('RGB',(1600,((len(pages)+7)//8)*300),'#dddddd')
draw=ImageDraw.Draw(master)
for i,f in enumerate(pages):
    im=Image.open(f).convert('RGB'); im.thumbnail((190,270))
    x=(i%8)*200+5; y=(i//8)*300+25
    master.paste(im,(x,y)); draw.text((x,y-23),str(i+1),font=font,fill='black')
master.save(out/'contact-all.png')
print(f'Rendered {len(pages)} pages; contact sheets: {out.resolve()}')
