
import re
import argparse


md_path = "book/checklist_mockup2.md"

HEADER3_RE = re.compile(r"^\s{0,3}###(?!#)\s+(.*\S)\s*$")
HEADER4_RE = re.compile(r"^\s{0,3}####(?!#)\s+(.*\S)\s*$")
LIST_ITEM_RE = re.compile(r"^\s*[-*]\s+(.*\S)\s*$")

AUTO_TABLE_START = "<!-- AUTO-TABLE:START -->"
AUTO_TABLE_END = "<!-- AUTO-TABLE:END -->"

def extract_checklist_sections(md_text):

    """
    Extracts only the text on lines that are Markdown level-3 headers.
    Returns a list of strings containing the header text (without the leading '###').

    Notes:
    - Matches lines like: "### Some title"
    - Does NOT match "####" (level-4 headers)
    - Does NOT include any text on following lines
    """
    titles = []
    for line in md_text.splitlines():
        match = HEADER3_RE.match(line)
        if match:
            titles.append(match.group(1).strip())
    return titles

def extract_checklist_levels(md_text):

    """
    Extracts only the text on lines that are Markdown level-4 headers.
    Returns a list of strings containing the header text (without the leading '####').

    Notes:
    - Matches lines like: "#### Some title"
    - Does NOT match "#####" (level-5 headers)
    - Does NOT include any text on following lines
    """
    levels = []
    for line in md_text.splitlines():
        match = HEADER4_RE.match(line)
        if match:
            levels.append(match.group(1).strip())
    return levels

def extract_list_items(md_text):
   
    """Extracts items from markdown lists (lines starting with '-' or '*').
    Returns a list of item strings."""
    
    # Match lines starting with '-' or '*', possibly with leading spaces
    pattern = r"^\s*[-*]\s+(.*)"
    items = re.findall(pattern, md_text, re.MULTILINE)
    return items


def extract_checklist_entries(md_text):

    """Extract checklist bullets grouped under ### section and #### level.

    Returns a list of dicts like:
      {"section": str, "level": str, "item": str}

    Notes:
    - Uses list-item pattern: r"^\s*[-*]\s+(.*)".
    - Only captures list items that appear after both a ### section and a #### level.
    - Continuation lines that are indented (e.g., wrapped bullet text) are appended.
    """

    entries = []
    current_section = None
    current_level = None
    last_entry_index = None

    for raw_line in md_text.splitlines():
        line = raw_line.rstrip("\n")

        match_section = HEADER3_RE.match(line)
        if match_section:
            current_section = match_section.group(1).strip()
            current_level = None
            last_entry_index = None
            continue

        match_level = HEADER4_RE.match(line)
        if match_level:
            current_level = match_level.group(1).strip()
            last_entry_index = None
            continue

        match_item = LIST_ITEM_RE.match(line)
        if match_item and current_section and current_level:
            entries.append(
                {
                    "section": current_section,
                    "level": current_level,
                    "item": match_item.group(1).strip(),
                }
            )
            last_entry_index = len(entries) - 1
            continue

        # If a bullet wraps onto the next line (indented), treat it as continuation.
        if last_entry_index is not None:
            if not line.strip():
                last_entry_index = None
                continue
            if line.startswith(" ") or line.startswith("\t"):
                entries[last_entry_index]["item"] += " " + line.strip()
            else:
                last_entry_index = None

    return entries


def _escape_md_table_cell(text: str) -> str:
    # Minimal escaping for Markdown tables.
    return text.replace("|", "\\|")


def entries_to_markdown_table(entries):
    """Format extracted entries as a Markdown table.

    Output columns match the checklist table in the markdown files:
      ID | Key Features | Level | Status
    """

    lines = []
    lines.append("| ID | Key Features | Level | Status |")
    lines.append("|---|---|---|---|")

    section_order = []
    section_to_index = {}
    section_item_counts = {}

    for entry in entries:
        section = entry["section"]
        if section not in section_to_index:
            section_order.append(section)
            section_to_index[section] = len(section_order)
            section_item_counts[section] = 0

        section_item_counts[section] += 1
        section_idx = section_to_index[section]
        item_idx = section_item_counts[section]
        entry_id = f"{section_idx}.{item_idx}"

        item_text = _escape_md_table_cell(entry["item"]) 
        level_text = _escape_md_table_cell(entry["level"]) 

        lines.append(f"| {entry_id} | {item_text} | {level_text} | [ ] |")

    return "\n".join(lines)


def update_details_block(md_text: str, table_md: str, summary_text: str = "Checklist") -> str:
    """Insert/replace an auto-generated table inside a <details> block.

    Targets the first <details> block containing a line like:
      <summary>Checklist</summary>

    If AUTO_TABLE markers exist inside that block, only replaces the region
    between them. Otherwise, inserts a new marked region just before </details>.
    """

    details_blocks = list(
        re.finditer(
            r"(?ms)^\s*<details>\s*$.*?^\s*</details>\s*$",
            md_text,
        )
    )

    if not details_blocks:
        raise ValueError("No <details>...</details> block found")

    target_match = None
    for match in details_blocks:
        block = match.group(0)
        if re.search(rf"(?m)^\s*<summary>\s*{re.escape(summary_text)}\s*</summary>\s*$", block):
            target_match = match
            break

    if target_match is None:
        raise ValueError(f"No <details> block found with <summary>{summary_text}</summary>")

    block = target_match.group(0)

    if AUTO_TABLE_START in block and AUTO_TABLE_END in block:
        start_idx = block.index(AUTO_TABLE_START) + len(AUTO_TABLE_START)
        end_idx = block.index(AUTO_TABLE_END)
        new_block = block[:start_idx] + "\n\n" + table_md.strip() + "\n\n" + block[end_idx:]
    else:
        # Insert just before closing tag.
        close_tag = re.search(r"(?m)^\s*</details>\s*$", block)
        if not close_tag:
            raise ValueError("Malformed <details> block: missing </details>")
        insert_at = close_tag.start()
        insertion = "\n\n" + AUTO_TABLE_START + "\n\n" + table_md.strip() + "\n\n" + AUTO_TABLE_END + "\n\n"
        new_block = block[:insert_at] + insertion + block[insert_at:]

    return md_text[: target_match.start()] + new_block + md_text[target_match.end() :]



def main() -> int:
    parser = argparse.ArgumentParser(description="Extract checklist bullets and generate a Markdown table.")
    parser.add_argument("--md", default=md_path, help="Path to the markdown file to parse")
    parser.add_argument("--summary", default="Checklist", help="<summary> text of the <details> block to update")
    parser.add_argument(
        "--write",
        action="store_true",
        help="Write the generated table back into the markdown file (updates/creates AUTO-TABLE region)",
    )
    args = parser.parse_args()

    # Read the markdown file
    with open(args.md, encoding="utf-8") as f:
        md_text = f.read()


#titles = extract_checklist_sections(md_text)
#for i, title in enumerate(titles, 1):
#    print(f"{i}: {title}")

#levels = extract_checklist_levels(md_text)
#for i, level in enumerate(levels, 1):
#    print(f"{level}")

    entries = extract_checklist_entries(md_text)
    table_md = entries_to_markdown_table(entries)

    if args.write:
        updated = update_details_block(md_text, table_md, summary_text=args.summary)
        with open(args.md, "w", encoding="utf-8", newline="\n") as f:
            f.write(updated)
        print(f"Updated details block in: {args.md}")
    else:
        print(table_md)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())