#!/usr/bin/env python3
"""
Split monolithic CyberSocium_Foundation_EN.md into separate section files
for MkDocs documentation site.
"""

import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EN_SOURCE = os.path.join(BASE_DIR, "CyberSocium_Foundation_EN.md")
DOCS_DIR = os.path.join(BASE_DIR, "site", "docs")

# Section mapping: (start_pattern, output_path, title, sidebar_position)
SECTIONS = [
    {
        "start": r"^# Section 1:",
        "end": r"^# Section 2:",
        "output": "theory/introduction.md",
        "title": "Introduction — Problem Statement",
        "description": "Crisis of institutions, data sovereignty, decentralization as historical trend",
    },
    {
        "start": r"^# Section 2:",
        "end": r"^# Section 3:",
        "output": "theory/literature-review.md",
        "title": "Literature Review",
        "description": "Political economy, common resources, cryptoeconomics, complex systems",
    },
    {
        "start": r"^# Section 3:",
        "end": r"^# Section 4:",
        "output": "theory/cybersocium-full.md",
        "title": "Theory of CyberSocium",
        "description": "Axioms, CyberSocial Corporation, PMIP, formal model",
    },
    {
        "start": r"^# Section 4:",
        "end": r"^# CyberSocium Foundation: Sections 5",
        "output": "architecture/full-spec.md",
        "title": "GyberExperiment Architecture",
        "description": "Technical specification — tokens, platforms, blockchain, DAO, legal, AI",
    },
    {
        "start": r"^# CyberSocium Foundation: Sections 5 & 6",
        "end": r"^# CyberSocium Foundation: Sections 7-12",
        "output": "ecosystem/sections-5-6.md",
        "title": "DAO Taxonomy & Ecosystem",
        "description": "Four-class DAO model and applied ecosystem",
    },
    {
        "start": r"^# CyberSocium Foundation: Sections 7-12",
        "end": None,  # Until end of file
        "output": "analysis/sections-7-12.md",
        "title": "Analysis, Discussion & Appendices",
        "description": "Comparative analysis, roadmap, conclusion, bibliography, appendices",
    },
]


def read_source():
    with open(EN_SOURCE, "r", encoding="utf-8") as f:
        return f.readlines()


def find_line(lines, pattern):
    for i, line in enumerate(lines):
        if re.match(pattern, line):
            return i
    return None


def extract_section(lines, start_pattern, end_pattern):
    start = find_line(lines, start_pattern)
    if start is None:
        print(f"  WARNING: Could not find start pattern: {start_pattern}")
        return ""

    if end_pattern:
        end = find_line(lines, end_pattern)
        if end is None:
            end = len(lines)
    else:
        end = len(lines)

    return "".join(lines[start:end]).strip()


def write_section(output_path, title, description, content):
    full_path = os.path.join(DOCS_DIR, output_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)

    header = f"""---
title: "{title}"
description: "{description}"
---

"""
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(header + content + "\n")

    print(f"  Written: {output_path} ({len(content)} chars)")


def main():
    print("Reading source document...")
    lines = read_source()
    print(f"  Total lines: {len(lines)}")

    print("\nSplitting into sections...")
    for section in SECTIONS:
        content = extract_section(lines, section["start"], section.get("end"))
        if content:
            write_section(
                section["output"],
                section["title"],
                section["description"],
                content,
            )

    print("\nDone! Section files created in site/docs/")


if __name__ == "__main__":
    main()
