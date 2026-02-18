#!/usr/bin/env python3
"""
Convert Mermaid .mmd files to SVG using Kroki API
"""

import base64
import os
import zlib
from pathlib import Path

import requests


def mermaid_to_svg(mermaid_code, output_path):
    """
    Convert Mermaid code to SVG using Kroki public API
    """
    # Encode the diagram using Kroki's compression format
    compressed = zlib.compress(mermaid_code.encode("utf-8"), 9)
    encoded = base64.urlsafe_b64encode(compressed).decode("ascii")

    # Call Kroki API
    url = f"https://kroki.io/mermaid/svg/{encoded}"

    print(f"Fetching SVG from Kroki API...")
    response = requests.get(url, timeout=30)

    if response.status_code == 200:
        # Save SVG to file
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(response.text)
        print(f"✓ Created: {output_path}")
        return True
    else:
        print(f"✗ Error: HTTP {response.status_code}")
        print(f"  Response: {response.text[:200]}")
        return False


def convert_all_diagrams():
    """
    Find all .mmd files and convert them to SVG
    """
    base_dir = Path("/Users/Gyber/GYBER_EXPERIMENT_DOCS/diagrams")

    # Find all .mmd files
    mmd_files = list(base_dir.rglob("*.mmd"))

    if not mmd_files:
        print("No .mmd files found")
        return

    print(f"Found {len(mmd_files)} Mermaid diagram(s) to convert\n")

    success_count = 0
    for mmd_file in mmd_files:
        print(f"Processing: {mmd_file.name}")

        # Read Mermaid code
        with open(mmd_file, "r", encoding="utf-8") as f:
            mermaid_code = f.read()

        # Generate output path
        svg_file = mmd_file.with_suffix(".svg")

        # Convert to SVG
        if mermaid_to_svg(mermaid_code, svg_file):
            success_count += 1

        print()

    print(f"Conversion complete: {success_count}/{len(mmd_files)} succeeded")


if __name__ == "__main__":
    try:
        convert_all_diagrams()
    except KeyboardInterrupt:
        print("\nConversion cancelled")
    except Exception as e:
        print(f"Error: {e}")
        import traceback

        traceback.print_exc()
