"""Extract missing lecture 2/3 figures from the original PDFs.

Usage: python scripts/extract_remaining_figures.py "path/to/lecture PDFs"
Requires Pillow and MiKTeX's pdftoppm. Crops use 480 x 270 slide coordinates.
"""
import argparse
from pathlib import Path
import subprocess

from PIL import Image

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("source_dir", type=Path)
args = parser.parse_args()
project = Path(__file__).resolve().parents[1]
cache = project / "out" / "missing_figures"
cache.mkdir(parents=True, exist_ok=True)
assets = project / "cv_assets"
sources = {"acquisition": "Encrypt 2 - Aquisition.pdf", "color": "Encrypt 3 - Color.pdf"}


def crop(lecture, page, box):
    prefix = cache / f"{lecture}-{page}"
    subprocess.run([
        "pdftoppm", "-f", str(page), "-l", str(page), "-singlefile",
        "-scale-to", "2400", "-png", str(args.source_dir / sources[lecture]),
        str(prefix),
    ], check=True, capture_output=True)
    with Image.open(prefix.with_suffix(".png")) as image:
        scale_x, scale_y = image.width / 480, image.height / 270
        return image.convert("RGB").crop(tuple(round(v * (scale_x if i % 2 == 0 else scale_y)) for i, v in enumerate(box)))


def save(name, image):
    image.save(assets / name, quality=96, subsampling=0)
    print(name)


first = crop("acquisition", 35, (124, 42, 357, 258))
second = crop("acquisition", 36, (63, 42, 357, 258))
combined = Image.new("RGB", (first.width + second.width + 40, first.height), "white")
combined.paste(first, (0, 0))
combined.paste(second, (first.width + 40, 0))
save("quantization_levels.jpg", combined)

figures = [
    ("spatial_resolution_effect.jpg", "acquisition", 51, (126, 42, 345, 264)),
    ("bicubic_vs_bilinear.jpg", "acquisition", 85, (65, 32, 414, 226)),
    ("source_spectra.jpg", "color", 8, (118, 70, 362, 270)),
    ("surface_reflectance_spectra.jpg", "color", 9, (108, 77, 419, 267)),
    ("cone_sensitivity.jpg", "color", 14, (101, 68, 417, 195)),
    ("metamer_spectra.jpg", "color", 17, (94, 43, 369, 267)),
    ("cie_xyz_chromaticity.jpg", "color", 28, (104, 142, 369, 263)),
    ("mcdam_ellipses.jpg", "color", 29, (102, 133, 375, 258)),
    ("hsv_model.jpg", "color", 31, (140, 74, 349, 233)),
    ("checker_shadow.jpg", "color", 38, (137, 61, 341, 222)),
    ("white_balance_example.jpg", "color", 46, (20, 120, 457, 243)),
    ("white_balance_mixed_illuminants.jpg", "color", 48, (127, 80, 356, 247)),
]
for name, lecture, page, box in figures:
    save(name, crop(lecture, page, box))
