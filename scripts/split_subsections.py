#!/usr/bin/env python3
"""
Further split Section 3 and Section 4 into subsection files,
and split Sections 5-6 and 7-12 into individual topic files.
"""

import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS_DIR = os.path.join(BASE_DIR, "site", "docs")


def read_file(path):
    with open(os.path.join(DOCS_DIR, path), "r", encoding="utf-8") as f:
        return f.readlines()


def write_file(path, title, description, content):
    full_path = os.path.join(DOCS_DIR, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    header = f'---\ntitle: "{title}"\ndescription: "{description}"\n---\n\n'
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(header + content.strip() + "\n")
    print(f"  Written: {path} ({len(content)} chars)")


def find_line(lines, pattern):
    for i, line in enumerate(lines):
        if re.match(pattern, line.strip()):
            return i
    return None


def extract_between(lines, start_idx, end_idx):
    if start_idx is None:
        return ""
    if end_idx is None:
        end_idx = len(lines)
    return "".join(lines[start_idx:end_idx]).strip()


def split_section3():
    print("Splitting Section 3...")
    lines = read_file("theory/cybersocium-full.md")

    # Skip frontmatter
    content_start = 0
    for i, line in enumerate(lines):
        if line.strip() == "---" and i > 0:
            content_start = i + 1
            if lines[content_start].strip() == "":
                content_start += 1
            break

    subsections = [
        (r"^## 3\.1\.", "theory/axioms.md", "Axiomatic Foundation",
         "The 12 fundamental axioms of CyberSocium", r"^## 3\.2\."),
        (r"^## 3\.2\.", "theory/cybersocial-corporation.md", "CyberSocial Corporation",
         "Definition and properties of a new economic unit", r"^## 3\.3\."),
        (r"^## 3\.3\.", "theory/evolution-of-forms.md", "Evolution of Forms",
         "Formalization of economic process management evolution", r"^## 3\.4\."),
        (r"^## 3\.4\.", "theory/pmip-selection.md", "PMIP & Socio-Economic Selection",
         "Principle of Minimum Individual Participation and selection mechanism", r"^## 3\.5\."),
        (r"^## 3\.5\.", "theory/directed-evolution.md", "Directed Evolution",
         "AI-directed evolution from blind to designed selection", r"^## 3\.6\."),
        (r"^## 3\.6\.", "theory/formal-model.md", "Formal Model",
         "CyberSocium as a complex adaptive system", None),
    ]

    for start_pat, output, title, desc, end_pat in subsections:
        start = find_line(lines, start_pat)
        end = find_line(lines, end_pat) if end_pat else None
        content = extract_between(lines, start, end)
        if content:
            write_file(output, title, desc, content)


def split_section4():
    print("Splitting Section 4...")
    lines = read_file("architecture/full-spec.md")

    subsections = [
        (r"^## 4\.1\.", "architecture/overview.md", "From Theory to Implementation",
         "Correspondence mapping between theory and architecture", r"^## 4\.2\."),
        (r"^## 4\.2\.", "architecture/tokenomics.md", "Tokenomics (GBR)",
         "GyberCommunityToken specification, emission, rewards, liquidity", r"^## 4\.3\."),
        (r"^## 4\.3\.", "architecture/gsp.md", "Gyber Social Platform",
         "Decentralized social platform architecture", r"^## 4\.4\."),
        (r"^## 4\.4\.", "architecture/gybernet.md", "GyberNet",
         "Community blockchain network", r"^## 4\.5\."),
        (r"^## 4\.5\.", "architecture/gybercomputer.md", "GyberComputer",
         "Distributed computing network", r"^## 4\.6\."),
        (r"^## 4\.6\.", "architecture/macroeconomic-dao.md", "MacroeconomicDAO",
         "Governance system with four classes of DAO", r"^## 4\.7\."),
        (r"^## 4\.7\.", "architecture/legal-duna.md", "Legal Framework (DUNA)",
         "Gybernaty DUNA legal structure and compliance", r"^## 4\.8\."),
        (r"^## 4\.8\.", "architecture/aic.md", "AiC — AI Department",
         "Artificial Intelligence Department architecture and governance", None),
    ]

    for start_pat, output, title, desc, end_pat in subsections:
        start = find_line(lines, start_pat)
        end = find_line(lines, end_pat) if end_pat else None
        content = extract_between(lines, start, end)
        if content:
            write_file(output, title, desc, content)


def split_sections_5_6():
    print("Splitting Sections 5 & 6...")
    lines = read_file("ecosystem/sections-5-6.md")

    subsections = [
        (r"^## 5\.", "dao/four-class-model.md", "DAO Taxonomy — Four-Class Model",
         "Overview of the four classes of decentralized decision-making", r"^### 5\.1\."),
        (r"^### 5\.1\.", "dao/social-dao.md", "Social DAO",
         "Community governance and social decision-making", r"^### 5\.2\."),
        (r"^### 5\.2\.", "dao/code-dao.md", "Code DAO",
         "Technical development and code governance", r"^### 5\.3\."),
        (r"^### 5\.3\.", "dao/commerce-dao.md", "Commerce DAO",
         "Commercial operations and business governance", r"^### 5\.4\."),
        (r"^### 5\.4\.", "dao/economic-dao.md", "Economic DAO",
         "Macroeconomic policy and resource allocation", r"^### 5\.5\."),
        (r"^### 5\.5\.", "dao/dao-interaction.md", "DAO Interaction & Conflict Resolution",
         "How the four DAO classes interact and resolve conflicts", r"^## 6\."),
        (r"^## 6\.", "ecosystem/applications.md", "Applied Ecosystem",
         "From theory to implementation — GSP, GyberNet, GyberComputer, G-Plan", None),
    ]

    for start_pat, output, title, desc, end_pat in subsections:
        start = find_line(lines, start_pat)
        end = find_line(lines, end_pat) if end_pat else None
        content = extract_between(lines, start, end)
        if content:
            write_file(output, title, desc, content)


def split_sections_7_12():
    print("Splitting Sections 7-12...")
    lines = read_file("analysis/sections-7-12.md")

    subsections = [
        (r"^## 7\.", "analysis/comparative.md", "Comparative Analysis",
         "Comparison with existing theoretical frameworks and practical projects", r"^## 8\."),
        (r"^## 8\.", "analysis/discussion.md", "Discussion",
         "Implications, limitations, and open questions", r"^## 9\."),
        (r"^## 9\.", "roadmap.md", "Roadmap",
         "From experiment to ecosystem — Foundation, Growth, Scaling, Maturity", r"^## 10\."),
        (r"^## 10\.", "appendices/conclusion.md", "Conclusion",
         "Summary and vision for the future", r"^## 11\."),
        (r"^## 11\.", "appendices/bibliography.md", "Bibliography",
         "Academic references and citations", r"^## 12\."),
        (r"^## 12\.", "appendices/appendices-combined.md", "Appendices",
         "Glossary, smart contract addresses, axioms summary", None),
    ]

    for start_pat, output, title, desc, end_pat in subsections:
        start = find_line(lines, start_pat)
        end = find_line(lines, end_pat) if end_pat else None
        content = extract_between(lines, start, end)
        if content:
            write_file(output, title, desc, content)


def main():
    split_section3()
    split_section4()
    split_sections_5_6()
    split_sections_7_12()
    print("\nAll subsections split successfully!")


if __name__ == "__main__":
    main()
