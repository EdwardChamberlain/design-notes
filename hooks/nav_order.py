"""MkDocs hooks for navigation ordering."""

from __future__ import annotations

import re
from typing import Iterable


LICENCE_URIS = {"licence.md", "license.md"}
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


def _is_licence_page(page: object) -> bool:
    file_obj = getattr(page, "file", None)
    src_uri = getattr(file_obj, "src_uri", "")
    return str(src_uri).lower() in LICENCE_URIS


def _move_matches_to_end(items: Iterable[object], matcher) -> list[object]:
    items_list = list(items)
    matches = [item for item in items_list if matcher(item)]
    if not matches:
        return items_list
    non_matches = [item for item in items_list if not matcher(item)]
    return non_matches + matches


def on_nav(nav, **kwargs):  # noqa: ANN001
    """Keep licence page last while preserving auto-generated nav."""
    nav.items = _move_matches_to_end(nav.items, _is_licence_page)
    nav.pages = _move_matches_to_end(nav.pages, _is_licence_page)
    return nav


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
    """Apply optional table highlight classes from markdown markers."""

    def _replace(match: re.Match[str]) -> str:
        raw_classes = match.group("classes")
        requested = [token.strip() for token in raw_classes.split() if token.strip()]
        classes = [token for token in requested if token in ALLOWED_TABLE_CLASSES]
        table_tag = match.group("table_tag")
        return _append_classes_to_table(table_tag, classes)

    return TABLE_CLASS_MARKER_RE.sub(_replace, html)
