"""Extract the lecture illustrations without changing their visual content.

Usage: python scripts/extract_figures.py "path/to/Encrypt 1 - Introduction.pdf"
Requires Pillow and the Poppler pdfimages/pdftoppm commands supplied by MiKTeX.
Crop coordinates refer to a 600-pixel-wide preview of each source slide.
"""
import argparse
import math
from pathlib import Path
import subprocess

from PIL import Image, ImageDraw, ImageFont, ImageOps

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("pdf", type=Path)
args = parser.parse_args()
source = args.pdf.resolve(strict=True)
project = Path(__file__).resolve().parents[1]
assets = project / "cv_assets"
cache = project / "out" / "extracted_slides"
assets.mkdir(exist_ok=True)
cache.mkdir(parents=True, exist_ok=True)
font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 36)
pages = {}


def crop(page, box):
    if page not in pages:
        prefix = cache / f"slide-{page:03}"
        subprocess.run([
            "pdftoppm", "-f", str(page), "-l", str(page), "-singlefile",
            "-scale-to", "1920", "-png", str(source), str(prefix),
        ], check=True, capture_output=True)
        pages[page] = Image.open(prefix.with_suffix(".png")).convert("RGB")
    im = pages[page]
    factor = im.width / 600
    return im.crop(tuple(round(c * factor) for c in box))


def save(name, im):
    im.save(assets / name, quality=96, subsampling=0)
    print(f"{name}: {im.width} x {im.height}")


def grid(name, panels, columns, cell=(800, 480)):
    width, height = cell
    rows = math.ceil(len(panels) / columns)
    canvas = Image.new("RGB", (columns * width, rows * height), "white")
    draw = ImageDraw.Draw(canvas)
    for i, (label, page, box) in enumerate(panels):
        x, y = (i % columns) * width, (i // columns) * height
        draw.text((x + width / 2, y + 22), label, font=font, fill="#601928", anchor="mm")
        im = ImageOps.contain(crop(page, box), (width - 24, height - 64), Image.Resampling.LANCZOS)
        canvas.paste(im, (x + (width - im.width) // 2, y + 52 + (height - 64 - im.height) // 2))
    save(name, canvas)


# Extract the original eye artwork, without the slide's overlaid title.
prefix = cache / "eye"
subprocess.run(["pdfimages", "-f", "15", "-l", "15", "-png", str(source), str(prefix)],
               check=True, capture_output=True)
eye_files = list(cache.glob("eye-*.png"))
eye = max((Image.open(p).convert("RGB") for p in eye_files), key=lambda im: im.width * im.height)
save("computer_vision_eye.jpg", eye)

save("visual_data_domains_tight.jpg", crop(17, (84, 55, 522, 337.5)))
save("nuisance_parameters_tight.jpg", crop(54, (97, 50, 499, 296)))
save("semantic_object_labels_tight.jpg", crop(47, (74, 36, 526, 337.5)))
save("stereo_geometry_tight.jpg", crop(101, (154, 83, 450, 322)))

grid("visual_cues_grid_tight.jpg", [
    ("Linear perspective", 63, (75, 45, 525, 337.5)),
    ("Aerial perspective", 64, (90, 36, 510, 337.5)),
    ("Texture gradient", 66, (90, 28, 510, 337.5)),
    ("Shading", 67, (90, 60, 513, 337.5)),
], columns=2, cell=(800, 530))

grid("history_grid_tight.jpg", [
    ("1960s: Synthetic worlds", 31, (76, 106, 513, 254)),
    ("1980s: Geometry", 34, (145, 101, 454, 294)),
    ("1990s: Statistical recognition", 35, (148, 107, 455, 294)),
    ("2000s: Data and recognition", 36, (146, 103, 454, 299)),
    ("2010s: Deep learning", 37, (80, 105, 525, 297)),
    ("2020s: Autonomous vehicles", 38, (155, 109, 445, 274)),
], columns=3, cell=(800, 450))

grid("early_vision_grid_tight.jpg", [
    ("Local filtering", 78, (73, 61, 527, 221)),
    ("Texture classification", 81, (95, 0, 511, 318)),
    ("Shape from texture", 82, (92, 93, 508, 277)),
], columns=3, cell=(800, 520))

grid("recognition_examples_tight.jpg", [
    ("People present: positive examples", 91, (124, 79, 476, 300)),
    ("No people: negative examples", 92, (98, 62, 491, 309)),
], columns=2, cell=(900, 620))

grid("applications_grid_tight.jpg", [
    ("Optical character recognition", 108, (101, 118, 494, 280)),
    ("Biometrics", 112, (118, 46, 490, 333)),
    ("Intelligent vehicles", 117, (121, 61, 501, 253)),
    ("Medical imaging", 121, (96, 76, 510, 282)),
], columns=2, cell=(900, 560))
