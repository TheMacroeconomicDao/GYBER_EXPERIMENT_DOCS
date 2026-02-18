#!/usr/bin/env python3
"""
Convert SVG diagrams to PNG at 300 DPI using cairosvg
"""

import sys
from pathlib import Path

try:
    import cairosvg
except ImportError:
    print("Error: cairosvg not installed")
    print("Install with: pip install cairosvg")
    sys.exit(1)


def svg_to_png(svg_path, png_path, dpi=300):
    """
    Convert SVG to PNG using cairosvg and set DPI metadata
    """
    try:
        import io

        from PIL import Image

        # Calculate scale factor for 300 DPI (default is 96 DPI)
        scale = dpi / 96.0

        # Convert SVG to PNG bytes
        png_bytes = cairosvg.svg2png(url=str(svg_path), scale=scale)

        # Open with PIL to set DPI metadata
        img = Image.open(io.BytesIO(png_bytes))

        # Save with DPI metadata
        img.save(png_path, dpi=(dpi, dpi))

        print(f"✓ Created: {png_path.name} ({img.size[0]}x{img.size[1]} @ {dpi} DPI)")
        return True
    except Exception as e:
        print(f"✗ Error converting {svg_path.name}: {e}")
        return False


def convert_all_svgs():
    """
    Find all SVG files and convert them to PNG at 300 DPI
    """
    base_dir = Path("/Users/Gyber/GYBER_EXPERIMENT_DOCS/diagrams")

    # Find all .svg files
    svg_files = list(base_dir.rglob("*.svg"))

    if not svg_files:
        print("No .svg files found")
        return

    print(f"Found {len(svg_files)} SVG diagram(s) to convert\n")

    success_count = 0
    for svg_file in svg_files:
        print(f"Processing: {svg_file.name}")

        # Generate output path
        png_file = svg_file.with_suffix(".png")

        # Convert to PNG
        if svg_to_png(svg_file, png_file, dpi=300):
            success_count += 1

    print(f"\nConversion complete: {success_count}/{len(svg_files)} succeeded")


if __name__ == "__main__":
    try:
        convert_all_svgs()
    except KeyboardInterrupt:
        print("\nConversion cancelled")
    except Exception as e:
        print(f"Error: {e}")
        import traceback

        traceback.print_exc()
