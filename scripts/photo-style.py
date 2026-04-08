#!/usr/bin/env python3
"""
Café Athena photo style processor.

Applies the Café Athena visual grade to a raw food photo:
  - Dark, moody exposure
  - Warm amber/brown color temperature
  - Deep blacks with dramatic shadows
  - Subtle vignette
  - Output as WebP

Usage:
    python3 scripts/photo-style.py <input> <output.webp>
    python3 scripts/photo-style.py IMG_1042.JPG site/public/images/03-14.webp
"""

import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageEnhance


def apply_style(input_path: str, output_path: str) -> None:
    img = Image.open(input_path).convert("RGB")
    arr = np.array(img, dtype=np.float32) / 255.0

    # 1. Warm color temperature: boost red, pull blue
    arr[:, :, 0] = np.clip(arr[:, :, 0] * 1.10, 0, 1)  # red up
    arr[:, :, 1] = np.clip(arr[:, :, 1] * 1.03, 0, 1)  # green slightly up
    arr[:, :, 2] = np.clip(arr[:, :, 2] * 0.82, 0, 1)  # blue down

    # 2. Exposure reduction — darken to moody level
    arr = np.clip(arr * 0.72, 0, 1)

    # 3. Tone curve — deepen shadows more than highlights (gamma > 1)
    arr = np.power(arr, 1.18)

    # 4. Contrast boost
    midpoint = 0.44
    arr = np.clip((arr - midpoint) * 1.30 + midpoint, 0, 1)

    img = Image.fromarray((arr * 255).astype(np.uint8))

    # 5. Slight saturation pull — muted but rich, not flat
    img = ImageEnhance.Color(img).enhance(0.88)

    # 6. Vignette — darken edges, center stays bright
    w, h = img.size
    cy, cx = h / 2.0, w / 2.0
    yx = np.mgrid[0:h, 0:w].astype(np.float32)
    dy = (yx[0] - cy) / cy
    dx = (yx[1] - cx) / cx
    vig = 1.0 - (dx ** 2 + dy ** 2) * 0.55
    vig = np.clip(vig, 0.45, 1.0)

    arr2 = np.array(img, dtype=np.float32) / 255.0
    arr2 *= vig[:, :, np.newaxis]
    img = Image.fromarray((arr2 * 255).astype(np.uint8))

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    img.save(output_path, "WEBP", quality=92)
    print(f"Saved → {output_path}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 scripts/photo-style.py <input> <output.webp>")
        sys.exit(1)
    apply_style(sys.argv[1], sys.argv[2])
