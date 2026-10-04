"""Restore lecture figures from the original PDFs (pypdf, Pillow, pdftoppm).

Usage: python extract_figures.py PATH_TO_SLIDE_FOLDER
The folder must contain 00.pdf and data_vectors.pdf.
Crop coordinates refer to an 800 x 450 preview of each slide.
"""
import argparse
import subprocess
from pathlib import Path
from pypdf import PdfReader

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('slides', type=Path)
args = parser.parse_args()
assets = Path(__file__).resolve().parent / 'assets'
assets.mkdir(exist_ok=True)

# filename, slide number, rectangle (left, top, right, bottom)
crops = {
    '00.pdf': [
        ('lifecycle', 18, (58, 112, 755, 415)),
        ('ai_ml_hierarchy', 19, (180, 201, 545, 439)),
        ('traditional_vs_ml', 26, (165, 197, 712, 404)),
        ('regression', 27, (9, 110, 790, 345)),
        ('graph_regression', 28, (9, 110, 790, 345)),
        ('text_classification', 29, (9, 110, 790, 345)),
        ('music_classification', 30, (9, 110, 790, 345)),
        ('image_classification', 31, (9, 110, 790, 345)),
        ('supervised_model', 32, (85, 103, 735, 365)),
        ('image_segmentation', 34, (9, 121, 790, 339)),
        ('depth_estimation', 35, (9, 110, 790, 342)),
        ('pose_estimation', 36, (9, 110, 790, 342)),
        ('translation', 37, (28, 144, 777, 377)),
        ('image_captioning', 38, (28, 144, 777, 377)),
        ('text_to_image', 39, (28, 144, 777, 377)),
        ('deepcluster', 43, (12, 35, 790, 430)),
        ('latent_variables', 47, (48, 115, 765, 398)),
    ],
    'data_vectors.pdf': [
        ('iris', 2, (182, 252, 613, 412)),
        ('vectors_visual', 12, (52, 209, 461, 399)),
    ],
}
for source, figures in crops.items():
    for name, page, (left, top, right, bottom) in figures:
        # Slides are 960 x 540 PDF points; 150 dpi gives a 2000 x 1125 image.
        scale = 2.5
        result = subprocess.run([
            'pdftoppm', '-f', str(page), '-l', str(page), '-singlefile',
            '-r', '150', '-x', str(round(left * scale)),
            '-y', str(round(top * scale)), '-W', str(round((right-left)*scale)),
            '-H', str(round((bottom-top)*scale)), '-png',
            str(args.slides / source), str(assets / name),
        ], capture_output=True, text=True)
        if result.returncode:
            raise RuntimeError(result.stderr)
        print(f'{name}.png <- {source}, slide {page}')

# Extract complete embedded diagrams directly to retain their native quality.
embedded = {
    '00.pdf': [
        ('generative_cats', 46, 0),
        ('rl_chess', 49, 0),
    ],
    'data_vectors.pdf': [
        ('basis_visual', 14, 0), ('standard_basis_example', 18, 0),
        ('nonstandard_basis_example', 22, 0), ('nonstandard_weights', 24, 0),
        ('encoded_data', 28, 0), ('subspace_3d', 31, 0),
        ('encoding_decoding', 34, 0), ('orthonormal_projection', 35, 0),
    ],
}
for source, figures in embedded.items():
    reader = PdfReader(args.slides / source)
    for name, page, index in figures:
        reader.pages[page-1].images[index].image.save(assets / f'{name}.png')
        print(f'{name}.png <- {source}, slide {page}, image {index}')
