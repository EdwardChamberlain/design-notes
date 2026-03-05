"""MkDocs hook for applying whitelisted classes to markdown tables."""

from __future__ import annotations

import re


TABLE_CLASS_MARKER_RE = re.compile(
    r"<!--\s*table-class:\s*(?P<classes>[^>]+?)\s*-->\s*(?P<table_tag><table\b[^>]*>)",
    flags=re.IGNORECASE,
)
ALLOWED_TABLE_CLASSES = {
    "table-hl-none",
    "table-hl-no-col",
    "table-hl-row-2",
    "table-hl-col-2",
}


def _append_classes_to_table(table_tag: str, classes: list[str]) -> str:
    if not classes:
        return table_tag

    classes_str = " ".join(classes)
    if 'class="' in table_tag:
        return re.sub(
            r'class="([^"]*)"',
            lambda match: f'class="{match.group(1)} {classes_str}"',
            table_tag,
            count=1,
        )
    return table_tag.replace("<table", f'<table class="{classes_str}"', 1)


def on_page_content(html: str, **kwargs) -> str:
    """Apply optional table classes declared in markdown comments."""

    def _replace(match: re.Match[str]) -> str:
        raw_classes = match.group("classes")
        requested = [token.strip() for token in raw_classes.split() if token.strip()]
        classes = [token for token in requested if token in ALLOWED_TABLE_CLASSES]
        table_tag = match.group("table_tag")
        return _append_classes_to_table(table_tag, classes)

    return TABLE_CLASS_MARKER_RE.sub(_replace, html)
