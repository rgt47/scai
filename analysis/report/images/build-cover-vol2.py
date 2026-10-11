#!/usr/bin/env python3
"""
Build the Volume II cover for Statistical Computing in the
Age of AI, in the visual idiom of the Springer Texts in
Statistics series: two-zone composition with a watercolor-
painted top zone and a solid bottom zone, clean sans-serif
typography.

Differs from the SCAI and practicum covers only in palette:
anchored on burgundy #7a2c4e (the former scai-advanced brand)
with warm rose, plum, and amber accents in the top zone.

Usage:
    python3 build-cover-vol2.py
Output:
    cover-vol2.png   (1200 x 1800, next to this script)
"""

import random
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont

# --- canvas ---------------------------------------------------------------

W, H        = 1200, 1800
SPLIT_Y     = int(H * 0.36)

# --- colours --------------------------------------------------------------

# brand burgundy anchors the bottom zone
BURG_DARK   = (122, 44, 78)         # #7a2c4e
BURG_DEEP   = (76, 24, 48)          # darker burgundy
CREAM       = (248, 244, 233)
GOLD        = (201, 169, 97)
INK         = (45, 55, 72)
WHITE       = (255, 255, 255)

# top-zone watercolor palette: deep wine through plum into
# warm rose and amber. complementary to the brand burgundy
# and visibly distinct from the practicum (teal-violet-coral)
# and the SCAI (navy-indigo-amber) covers.
WATERCOLOUR = [
    (76,  24,  48),    # deep wine
    (122, 44,  78),    # burgundy
    (160, 76, 110),    # plum rose
    (208, 130, 130),   # warm rose
    (228, 178,  98),   # warm amber
]

# --- helpers --------------------------------------------------------------

def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def palette_at(t, palette=WATERCOLOUR):
    n = len(palette) - 1
    pos = t * n
    i   = int(pos)
    if i >= n:
        return palette[-1]
    return lerp(palette[i], palette[i + 1], pos - i)


def watercolor_zone(width, height, seed=71):
    """
    Build a soft watercolor-style gradient by drawing many
    overlapping radial blobs across the canvas.
    """
    rng  = random.Random(seed)
    base = Image.new('RGB', (width, height), (240, 240, 240))
    px   = base.load()

    for y in range(height):
        for x in range(width):
            t = (x / width * 0.55 + y / height * 0.45)
            t = max(0.0, min(1.0, t))
            px[x, y] = palette_at(t)

    overlay = Image.new('RGB', (width, height), (0, 0, 0))
    odraw   = ImageDraw.Draw(overlay)
    mask    = Image.new('L', (width, height), 0)
    mdraw   = ImageDraw.Draw(mask)

    for _ in range(28):
        cx = rng.randint(-100, width + 100)
        cy = rng.randint(-50, height + 50)
        r  = rng.randint(180, 480)
        col = palette_at(rng.uniform(0, 1))
        odraw.ellipse((cx - r, cy - r, cx + r, cy + r), fill=col)
        mdraw.ellipse((cx - r, cy - r, cx + r, cy + r), fill=70)

    overlay = overlay.filter(ImageFilter.GaussianBlur(radius=120))
    mask    = mask.filter(ImageFilter.GaussianBlur(radius=80))
    base    = Image.composite(overlay, base, mask)

    base    = base.filter(ImageFilter.GaussianBlur(radius=2))
    return base


def add_paper_grain(img, strength=8, seed=11):
    rng    = random.Random(seed)
    grain  = Image.new('L', img.size, 128)
    gpx    = grain.load()
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            gpx[x, y] = max(0, min(255, 128 + rng.randint(-strength, strength)))
    grain = grain.filter(ImageFilter.GaussianBlur(radius=0.5))
    img.paste(Image.blend(img.convert('RGB'),
                          Image.merge('RGB', (grain, grain, grain)),
                          0.05))
    return img


def font(name, size):
    candidates = {
        'avenir-medium':   ('/System/Library/Fonts/Avenir.ttc', 2),
        'avenir-heavy':    ('/System/Library/Fonts/Avenir.ttc', 6),
        'avenir-black':    ('/System/Library/Fonts/Avenir.ttc', 7),
        'avenir-book':     ('/System/Library/Fonts/Avenir.ttc', 1),
        'avenir-light':    ('/System/Library/Fonts/Avenir.ttc', 0),
        'helvetica-bold':  ('/System/Library/Fonts/Helvetica.ttc', 1),
        'helvetica':       ('/System/Library/Fonts/Helvetica.ttc', 0),
    }
    path, idx = candidates[name]
    return ImageFont.truetype(path, size, index=idx)


def draw_text(draw, xy, text, fnt, fill, anchor='lt'):
    draw.text(xy, text, font=fnt, fill=fill, anchor=anchor)


# --- build ---------------------------------------------------------------

def build():
    canvas = Image.new('RGB', (W, H), BURG_DARK)

    top = watercolor_zone(W, SPLIT_Y, seed=71)
    canvas.paste(top, (0, 0))

    draw = ImageDraw.Draw(canvas)

    # cream hairline divider
    draw.rectangle((0, SPLIT_Y, W, SPLIT_Y + 3), fill=CREAM)

    # left-edge spine accent
    draw.rectangle((0, 0, 14, SPLIT_Y), fill=BURG_DEEP)
    draw.rectangle((14, 0, 17, SPLIT_Y), fill=CREAM)

    # --- top-zone typography ---------------------------------------------
    series_fnt = font('avenir-heavy', 36)
    draw_text(draw, (60, 90),
              'GRADUATE BIOSTATISTICS SERIES',
              series_fnt, WHITE)

    author_fnt = font('avenir-medium', 64)
    authors = ['rgtlab Curriculum Project']
    y = 240
    for line in authors:
        draw_text(draw, (60, y), line, author_fnt, WHITE)
        y += 76

    # --- bottom-zone typography -------------------------------------------
    title_fnt   = font('avenir-black', 122)
    title_lines = ['Statistical', 'Computing', 'in the Age of AI']
    y = SPLIT_Y + 80
    for line in title_lines:
        draw_text(draw, (60, y), line, title_fnt, WHITE)
        y += 138

    sub_fnt = font('avenir-medium', 50)
    y += 24
    for line in ['Volume II',
                 'Advanced Methods and',
                 'Scientific Software']:
        draw_text(draw, (62, y), line, sub_fnt, CREAM)
        y += 64

    edition_fnt  = font('avenir-light', 46)
    edition_text = 'First Edition  ·  2026'
    draw_text(draw, (60, H - 200), edition_text, edition_fnt, CREAM)

    mark_fnt = font('avenir-heavy', 44)
    draw_text(draw, (W - 60, H - 80), 'rgtlab', mark_fnt, WHITE,
              anchor='rs')
    draw.rectangle((W - 240, H - 64, W - 60, H - 60), fill=GOLD)

    canvas = add_paper_grain(canvas)
    return canvas


if __name__ == '__main__':
    img = build()
    out = str(Path(__file__).resolve().parent / 'cover-vol2.png')
    img.save(out, optimize=True)
    print(f'wrote {out} ({img.size[0]} x {img.size[1]})')
