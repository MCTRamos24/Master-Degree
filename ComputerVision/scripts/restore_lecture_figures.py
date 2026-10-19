"""Restore lecture 6--9 illustrations from the original supplied PDFs.
Usage: python scripts/restore_lecture_figures.py "path/to/lecture PDFs"
Crop boxes use a 480 x 270 slide coordinate system and exclude slide headings.
"""
import argparse
from pathlib import Path
import subprocess
from PIL import Image, ImageDraw, ImageFont, ImageOps

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('source_dir',type=Path)
args=parser.parse_args()
project=Path(__file__).resolve().parents[1]
cache=project/'out'/'restored_slides'; cache.mkdir(parents=True,exist_ok=True)
assets=project/'cv_assets'; assets.mkdir(exist_ok=True)
names={6:'Edge',7:'Blobs',8:'Fitting',9:'Alignment'}
font=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',34)
pages={}
def crop(n,p,box):
    if (n,p) not in pages:
        prefix=cache/f'{n}-{p}'
        if not prefix.with_suffix('.png').exists():
            subprocess.run(['pdftoppm','-f',str(p),'-l',str(p),'-singlefile','-scale-to','2400','-png',str(args.source_dir/f'Encrypt {n} - {names[n]}.pdf'),str(prefix)],check=True,capture_output=True)
        pages[n,p]=Image.open(prefix.with_suffix('.png')).convert('RGB')
    im=pages[n,p]
    return im.crop(tuple(round(v*(im.width/480 if i%2==0 else im.height/270)) for i,v in enumerate(box)))
def save(name,panels,columns=1):
    ims=[(label,crop(n,p,b)) for label,n,p,b in panels]
    if len(ims)==1:
        result=ims[0][1]
    else:
        w=1050; h=max(round(im.height*min((w-30)/im.width,750/im.height)) for _,im in ims)+75
        result=Image.new('RGB',(columns*w,((len(ims)+columns-1)//columns)*h),'white'); draw=ImageDraw.Draw(result)
        for i,(label,im) in enumerate(ims):
            im=ImageOps.contain(im,(w-30,h-75),Image.Resampling.LANCZOS)
            x=(i%columns)*w; y=(i//columns)*h
            draw.text((x+w/2,y+12),label,font=font,fill='#7a1737',anchor='mt')
            result.paste(im,(x+(w-im.width)//2,y+65))
    result.save(assets/name,quality=96,subsampling=0)
    print(name, result.size,flush=True)

save('edge_smooth_first.jpg',[('',6,11,(85,43,346,233))])
save('edge_canny_stages.jpg',[(label,6,p,(153,47,330,224)) for label,p in [('Original',24),('Gradient magnitude',25),('Thresholded',26),('Thinned',27)]],2)
save('edge_hysteresis.jpg',[('',6,28,(57,44,422,256))])
save('edge_sigma_effect.jpg',[('',6,29,(60,75,419,210))])
save('harris_results.jpg',[('',7,27,(78,48,403,259))])
save('blob_scale_space_example.jpg',[(label,7,p,(136,68,345,218)) for label,p in [('Original',48),('Detected blobs',50)]],2)
save('blob_affine_adaptation.jpg',[(label,7,p,(129,60,357,230)) for label,p in [('Scale-invariant regions',60),('Affine-adapted regions',61)]],2)
save('feature_extraction_summary.jpg',[('',7,62,(57,72,420,234))])
save('hough_basic.jpg',[('',8,14,(65,40,408,236))])
save('robust_loss_source.jpg',[('',8,37,(73,105,284,260))])
save('ransac_line_sequence.jpg',[(label,8,p,(180,54,350,163)) for label,p in [('Sample',46),('Hypothesis',47),('Inlier test',48),('Refined model',49)]],2)
save('incremental_line_fitting.jpg',[(label,8,p,(65,85,372,233)) for label,p in [('Grow first segment',58),('Start next segment',59),('Final segments',61)]],3)
save('klines_sequence.jpg',[(label,8,p,(82,85,357,209)) for label,p in [('Initialize',64),('Assign',65),('Refit',66)]],3)
save('sift_descriptor.jpg',[('',9,25,(138,150,348,225))])
save('alignment_ransac_translation.jpg',[(label,9,p,(125,33,374,235)) for label,p in [('Putative matches',37),('Count inliers',38),('Refine translation',39)]],3)
save('alignment_hough_edges.jpg',[(label,9,p,box) for label,p,box in [('Image and Canny edges',53,(107,33,426,248)),('Hough votes',54,(67,42,387,252)),('Detected lines',55,(50,45,381,256))]],3)
save('panorama_results.jpg',[('',9,71,(57,51,401,267))])
save('pyramid_blending.jpg',[('',9,72,(67,39,414,227))])
save('gain_compensation.jpg',[('',9,74,(60,117,422,270))])
