#!/usr/bin/env python3
"""Batch-convert project line drawings into dark-mode and light-mode assets."""

from __future__ import annotations

import sys
from pathlib import Path

try:
    from PIL import Image, ImageChops
except ImportError:  # pragma: no cover - runtime dependency guard
    sys.stderr.write(
        "Missing dependency: Pillow\n"
        "Install it in the project virtual environment, for example:\n"
        "  env/bin/pip install Pillow\n"
    )
    raise SystemExit(1)

ROOT_DIR = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT_DIR / "docs/assets/images/line_drawings"
OVERWRITE = True
ALPHA_CROP_THRESHOLD = 8


def output_path_for(input_path: Path, suffix: str) -> Path:
    return input_path.with_name(f"{input_path.stem}{suffix}.png")


def build_alpha_mask(image: Image.Image) -> Image.Image:
    rgba = image.convert("RGBA")

    # Flatten any existing transparency onto white so the brightness-to-alpha
    # conversion behaves like a white drawing sheet.
    white_bg = Image.new("RGBA", rgba.size, (255, 255, 255, 255))
    flattened = Image.alpha_composite(white_bg, rgba)
    grayscale = flattened.convert("L")
    alpha = ImageChops.invert(grayscale)
    return alpha.point(lambda value: 0 if value < ALPHA_CROP_THRESHOLD else value)


def crop_to_content(image: Image.Image) -> Image.Image:
    alpha = image.getchannel("A")
    bounds = alpha.getbbox()
    if bounds is None:
        return image
    return image.crop(bounds)


def convert_image(input_path: Path, output_path: Path, rgb: tuple[int, int, int]) -> None:
    with Image.open(input_path) as image:
        alpha = build_alpha_mask(image)
        result = Image.new("RGBA", image.size, (*rgb, 255))
        result.putalpha(alpha)
        crop_to_content(result).save(output_path)


def source_images(directory: Path) -> list[Path]:
    allowed_suffixes = {".png", ".jpg", ".jpeg", ".bmp", ".tif", ".tiff", ".webp"}
    return sorted(
        path
        for path in directory.iterdir()
        if path.is_file()
        and path.suffix.lower() in allowed_suffixes
        and not path.stem.endswith(("_dark_mode", "_light_mode"))
    )


def main() -> int:
    source_dir = SOURCE_DIR

    if not source_dir.is_dir():
        sys.stderr.write(f"Input directory not found: {source_dir}\n")
        return 1

    images = source_images(source_dir)
    if not images:
        sys.stderr.write(f"No source images found in: {source_dir}\n")
        return 1

    for input_path in images:
        outputs = (
            (output_path_for(input_path, "_dark_mode"), (255, 255, 255)),
            (output_path_for(input_path, "_light_mode"), (0, 0, 0)),
        )

        for output_path, rgb in outputs:
            existed_before = output_path.exists()
            if existed_before and not OVERWRITE:
                print(f"Skipped {output_path} (already exists)")
                continue
            convert_image(input_path, output_path, rgb)
            if existed_before and OVERWRITE:
                print(f"Overwrote {output_path}")
            else:
                print(f"Wrote {output_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
