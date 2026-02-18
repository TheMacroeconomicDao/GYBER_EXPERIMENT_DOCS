#!/usr/bin/env python3
"""
Convert SVG diagrams to PNG at 300 DPI for PDF embedding
"""

import subprocess
from pathlib import Path


def svg_to_png(svg_path, png_path, dpi=300):
    """
    Convert SVG to PNG using ImageMagick or rsvg-convert
    """
    # Try rsvg-convert first (better quality)
    try:
        cmd = [
            "rsvg-convert",
            "-d",
            str(dpi),
            "-p",
            str(dpi),
            "-o",
            str(png_path),
            str(svg_path),
        ]
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(f"✓ Created: {png_path.name}")
        return True
    except FileNotFoundError:
        # Try ImageMagick convert as fallback
        try:
            cmd = [
                "convert",
                "-density",
                str(dpi),
                "-background",
                "white",
                "-alpha",
                "remove",
                str(svg_path),
                str(png_path),
            ]
            result = subprocess.run(cmd, check=True, capture_output=True, text=True)
            print(f"✓ Created: {png_path.name}")
            return True
        except FileNotFoundError:
            print(f"✗ Error: Neither rsvg-convert nor ImageMagick convert found")
            print("  Please install one of these tools:")
            print("  - brew install librsvg (for rsvg-convert)")
            print("  - brew install imagemagick (for convert)")
            return False
        except subprocess.CalledProcessError as e:
            print(f"✗ Error converting {svg_path.name}: {e.stderr}")
            return False
    except subprocess.CalledProcessError as e:
        print(f"✗ Error converting {svg_path.name}: {e.stderr}")
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

        print()

    print(f"Conversion complete: {success_count}/{len(svg_files)} succeeded")


if __name__ == "__main__":
    try:
        convert_all_svgs()
    except KeyboardInterrupt:
        print("\nConversion cancelled")
    except Exception as e:
        print(f"Error: {e}")
        import traceback

        traceback.print_exc()
