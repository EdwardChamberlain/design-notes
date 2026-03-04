"""MkDocs hooks for navigation ordering."""

from __future__ import annotations

from typing import Iterable


LICENCE_URIS = {"licence.md", "license.md"}


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
