"""
Scrapes course section data from anthropic.skilljar.com and enriches
courseOverview.json with structured section info in English and German.

Output: data/courseDetails.json
"""

import json
import os
import re
import sys
from pathlib import Path

import anthropic
import requests
from dotenv import load_dotenv

ROOT = Path(__file__).parent.parent
load_dotenv(ROOT / ".env")

SKILLJAR_URL = "https://anthropic.skilljar.com/claude-with-the-anthropic-api"
COURSE_OVERVIEW_PATH = ROOT / "data" / "courseOverview.json"
OUTPUT_PATH = ROOT / "data" / "courseDetails.json"


# ---------------------------------------------------------------------------
# Anthropic client (Foundry or standard)
# ---------------------------------------------------------------------------

def make_client() -> anthropic.Anthropic:
    base_url = os.getenv("ANTHROPIC_BASE_URL")
    api_key = os.getenv("ANTHROPIC_FOUNDRY_API_KEY") or os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        sys.exit("No API key found. Set ANTHROPIC_API_KEY or ANTHROPIC_FOUNDRY_API_KEY in .env")
    kwargs = {"api_key": api_key}
    if base_url:
        kwargs["base_url"] = base_url
    return anthropic.Anthropic(**kwargs)


# ---------------------------------------------------------------------------
# Scraping
# ---------------------------------------------------------------------------

def fetch_page(url: str) -> str:
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    return r.text


def _clean_js_string(raw: str) -> str:
    """Remove surrounding quotes, unescape common JS escapes."""
    raw = raw.strip().rstrip(",")
    # Join multi-line string concatenations: "foo" +\n  "bar"
    raw = re.sub(r'"\s*\+\s*\n\s*"', "", raw)
    # Strip outer quotes
    if (raw.startswith('"') and raw.endswith('"')) or \
       (raw.startswith("'") and raw.endswith("'")):
        raw = raw[1:-1]
    elif raw.startswith("`") and raw.endswith("`"):
        raw = raw[1:-1]
    return raw.replace('\\"', '"').replace("\\'", "'").replace("\\n", "\n")


def _extract_string_field(block: str, field: str) -> str:
    """Extract a simple string field from a JS object block."""
    pattern = rf'{field}\s*:\s*((?:"(?:[^"\\]|\\.)*"|\'(?:[^\'\\]|\\.)*\'|`(?:[^`\\]|\\.)*`)(?:\s*\+\s*\n\s*(?:"(?:[^"\\]|\\.)*"|\'(?:[^\'\\]|\\.)*\'))*)'
    m = re.search(pattern, block, re.DOTALL)
    if not m:
        return ""
    return _clean_js_string(m.group(1))


def _extract_number_field(block: str, field: str) -> float | None:
    m = re.search(rf'{field}\s*:\s*([0-9]+(?:\.[0-9]+)?)', block)
    return float(m.group(1)) if m else None


def _extract_sections(block: str) -> list[dict]:
    """Extract the sections array from a course JS object block."""
    # Find sections: [ ... ] — grab content between first [ and matching ]
    m = re.search(r'sections\s*:\s*\[', block)
    if not m:
        return []
    start = m.end()
    depth = 1
    i = start
    while i < len(block) and depth > 0:
        if block[i] == "[":
            depth += 1
        elif block[i] == "]":
            depth -= 1
        i += 1
    sections_raw = block[start : i - 1]

    sections = []
    # Split into individual { ... } section objects
    obj_pattern = re.compile(r'\{', re.DOTALL)
    pos = 0
    while pos < len(sections_raw):
        m2 = obj_pattern.search(sections_raw, pos)
        if not m2:
            break
        obj_start = m2.start()
        depth = 1
        j = m2.end()
        while j < len(sections_raw) and depth > 0:
            if sections_raw[j] == "{":
                depth += 1
            elif sections_raw[j] == "}":
                depth -= 1
            j += 1
        obj_block = sections_raw[obj_start : j]
        pos = j

        section_id = _extract_string_field(obj_block, "id")
        title = _extract_string_field(obj_block, "title")
        description = _extract_string_field(obj_block, "description")
        lesson_count = _extract_number_field(obj_block, "lessonCount")

        if title:
            sections.append({
                "id": section_id,
                "title": title,
                "lessonCount": int(lesson_count) if lesson_count is not None else None,
                "description": description,
            })

    return sections


def parse_all_courses(html: str) -> dict[str, dict]:
    """
    Returns a dict keyed by course path (e.g. '/claude-with-the-anthropic-api')
    containing parsed course data.
    """
    # Each course block: const <name> = { ... };\nwindow._clpdata[...] = <name>;
    const_starts = [m.start() for m in re.finditer(r'\nconst \w+ = \{', html)]
    clpdata_marks = [m.start() for m in re.finditer(r'window\._clpdata\[', html)]

    courses = {}
    for i, start in enumerate(const_starts):
        # Block ends just after the matching window._clpdata assignment
        end = clpdata_marks[i] + 500 if i < len(clpdata_marks) else start + 50000
        block = html[start:end]

        path = _extract_string_field(block, "path")
        if not path:
            continue

        title = _extract_string_field(block, "title")
        subtitle = _extract_string_field(block, "subtitle")
        lecture_count = _extract_number_field(block, "lectureCount")
        video_hours = _extract_number_field(block, "videoHours")
        quiz_count = _extract_number_field(block, "quizCount")
        sections = _extract_sections(block)

        courses[path] = {
            "path": path,
            "title": title,
            "subtitle": subtitle,
            "stats": {
                k: v for k, v in {
                    "lectureCount": int(lecture_count) if lecture_count else None,
                    "videoHours": video_hours,
                    "quizCount": int(quiz_count) if quiz_count else None,
                }.items() if v is not None
            },
            "sections": sections,
        }

    return courses


# ---------------------------------------------------------------------------
# Translation
# ---------------------------------------------------------------------------

TRANSLATE_PROMPT = """\
Translate the following JSON from English to German. Keep JSON structure and keys unchanged.
Only translate string values. Preserve HTML tags, URLs, and proper nouns (course/product names
like Claude, Anthropic, MCP, Skilljar, etc.).
Return only the translated JSON, no explanation."""


def translate_to_german(client: anthropic.Anthropic, data: dict) -> dict:
    """Translate all translatable string fields of a course dict to German."""
    translatable = {
        "title": data.get("title", ""),
        "subtitle": data.get("subtitle", ""),
        "sections": [
            {"id": s["id"], "title": s["title"], "description": s["description"]}
            for s in data.get("sections", [])
        ],
    }
    payload = json.dumps(translatable, ensure_ascii=False)

    msg = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=4096,
        messages=[
            {
                "role": "user",
                "content": f"{TRANSLATE_PROMPT}\n\n{payload}",
            }
        ],
    )

    response_text = msg.content[0].text.strip()
    # Strip markdown code fences if present
    response_text = re.sub(r'^```(?:json)?\s*', '', response_text)
    response_text = re.sub(r'\s*```$', '', response_text)

    try:
        translated = json.loads(response_text)
    except json.JSONDecodeError:
        # Retry once with an explicit instruction to return only valid JSON
        retry_msg = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=4096,
            messages=[
                {"role": "user", "content": f"{TRANSLATE_PROMPT}\n\n{payload}"},
                {"role": "assistant", "content": response_text},
                {"role": "user", "content": "The JSON above is invalid. Return only the corrected, complete JSON with no extra text."},
            ],
        )
        response_text = retry_msg.content[0].text.strip()
        response_text = re.sub(r'^```(?:json)?\s*', '', response_text)
        response_text = re.sub(r'\s*```$', '', response_text)
        translated = json.loads(response_text)

    # Merge lesson counts back (not translatable)
    orig_sections = data.get("sections", [])
    for i, s in enumerate(translated.get("sections", [])):
        if i < len(orig_sections):
            s["lessonCount"] = orig_sections[i].get("lessonCount")

    return translated


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("Fetching Skilljar page…")
    html = fetch_page(SKILLJAR_URL)
    print(f"  Page size: {len(html):,} bytes")

    print("Parsing course data…")
    scraped = parse_all_courses(html)
    print(f"  Found {len(scraped)} courses with section data")

    with open(COURSE_OVERVIEW_PATH) as f:
        overview = json.load(f)

    client = make_client()

    result = []
    for course in overview["courseOverview"]:
        path = "/" + course["id"]
        scraped_data = scraped.get(path, {})

        print(f"\nProcessing: {course['title']}")

        en_data = {
            "title": scraped_data.get("title") or course["title"],
            "subtitle": scraped_data.get("subtitle") or course["description"],
            "sections": scraped_data.get("sections", []),
        }

        if scraped_data:
            print(f"  Translating {len(en_data['sections'])} sections to German…")
            de_data = translate_to_german(client, en_data)
        else:
            print("  No section data found, translating title/description only…")
            de_data = translate_to_german(client, en_data)

        entry = {
            "id": course["id"],
            "path": path,
            "link": course["link"],
            "stats": scraped_data.get("stats", {}),
            "en": en_data,
            "de": de_data,
        }
        result.append(entry)

    output = {"courseDetails": result}
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"\nSaved to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
