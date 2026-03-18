"""MkDocs hook for applying markdown table classes and table merge markers."""

from __future__ import annotations

import re
from dataclasses import dataclass


TABLE_CLASS_MARKER_RE = re.compile(
    r"<!--\s*table-class:\s*(?P<classes>[^>]+?)\s*-->\s*(?P<table_tag><table\b[^>]*>)",
    flags=re.IGNORECASE,
)
TABLE_RE = re.compile(r"<table\b[^>]*>.*?</table>", flags=re.IGNORECASE | re.DOTALL)
ROW_RE = re.compile(
    r"(?P<open><tr\b[^>]*>)(?P<body>.*?)(?P<close></tr>)",
    flags=re.IGNORECASE | re.DOTALL,
)
CELL_RE = re.compile(
    r"(?P<open><(?P<tag>t[dh])\b(?P<attrs>[^>]*)>)(?P<content>.*?)(?P<close></(?P=tag)>)",
    flags=re.IGNORECASE | re.DOTALL,
)
ROWSPAN_UP_RE = re.compile(
    r"^\s*(?:\[\[ROWSPAN-UP\]\]|<(?:rowspan-up|colspan-up)\s*/?>\s*(?:</(?:rowspan-up|colspan-up)>\s*)?)$",
    flags=re.IGNORECASE | re.DOTALL,
)
COLSPAN_LEFT_RE = re.compile(
    r"^\s*(?:\[\[COLSPAN-LEFT\]\]|<(?:colspan-left|rowspan-left)\s*/?>\s*(?:</(?:colspan-left|rowspan-left)>\s*)?)$",
    flags=re.IGNORECASE | re.DOTALL,
)
ROWSPAN_ATTR_RE = re.compile(r'\srowspan="(?P<value>\d+)"', flags=re.IGNORECASE)
COLSPAN_ATTR_RE = re.compile(r'\scolspan="(?P<value>\d+)"', flags=re.IGNORECASE)
CLASS_ATTR_RE = re.compile(r'class="(?P<value>[^"]*)"', flags=re.IGNORECASE)
MERGE_MARKDOWN_RE = re.compile(
    r"<(?P<name>rowspan-up|colspan-up|colspan-left|rowspan-left)\s*/?>",
    flags=re.IGNORECASE,
)
ROWSPAN_SENTINEL = "[[ROWSPAN-UP]]"
COLSPAN_LEFT_SENTINEL = "[[COLSPAN-LEFT]]"
ALLOWED_TABLE_CLASSES = {
    "table-hl-no-row",
    "table-hl-no-col",
    "table-hl-row-2",
    "table-hl-col-2",
    "table-layout-auto",
    "table-width-full",
    "table-divider-cols",
    "table-divider-rows",
}


@dataclass
class TableCell:
    tag: str
    attrs: str
    content: str
    rowspan: int = 1
    colspan: int = 1
    logical_col: int | None = None

    @classmethod
    def from_match(cls, match: re.Match[str]) -> "TableCell":
        attrs = match.group("attrs")
        rowspan_match = ROWSPAN_ATTR_RE.search(attrs)
        colspan_match = COLSPAN_ATTR_RE.search(attrs)
        rowspan = int(rowspan_match.group("value")) if rowspan_match else 1
        colspan = int(colspan_match.group("value")) if colspan_match else 1
        return cls(
            tag=match.group("tag"),
            attrs=attrs,
            content=match.group("content"),
            rowspan=rowspan,
            colspan=colspan,
        )

    def render(self) -> str:
        attrs = ROWSPAN_ATTR_RE.sub("", self.attrs)
        attrs = COLSPAN_ATTR_RE.sub("", attrs)
        if self.logical_col == 1:
            attrs = _append_class(attrs, "table-col-1")
        if self.rowspan > 1:
            attrs = f'{attrs} rowspan="{self.rowspan}"'
        if self.colspan > 1:
            attrs = f'{attrs} colspan="{self.colspan}"'
        return f"<{self.tag}{attrs}>{self.content}</{self.tag}>"


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


def _append_class(attrs: str, class_name: str) -> str:
    class_match = CLASS_ATTR_RE.search(attrs)
    if class_match:
        classes = class_match.group("value").split()
        if class_name in classes:
            return attrs
        return CLASS_ATTR_RE.sub(
            f'class="{class_match.group("value")} {class_name}"',
            attrs,
            count=1,
        )
    return f'{attrs} class="{class_name}"'


def _apply_table_classes(html: str) -> str:
    def _replace(match: re.Match[str]) -> str:
        raw_classes = match.group("classes")
        requested = [token.strip() for token in raw_classes.split() if token.strip()]
        classes = [token for token in requested if token in ALLOWED_TABLE_CLASSES]
        table_tag = match.group("table_tag")
        return _append_classes_to_table(table_tag, classes)

    return TABLE_CLASS_MARKER_RE.sub(_replace, html)


def _apply_rowspan_markers(table_html: str) -> str:
    row_prefixes: list[str] = []
    rows: list[tuple[str, list[TableCell], str]] = []
    last_end = 0

    for match in ROW_RE.finditer(table_html):
        row_prefixes.append(table_html[last_end:match.start()])
        cells = [TableCell.from_match(cell_match) for cell_match in CELL_RE.finditer(match.group("body"))]
        rows.append((match.group("open"), cells, match.group("close")))
        last_end = match.end()

    if not rows:
        return table_html

    anchors: dict[int, TableCell] = {}
    filtered_rows: list[tuple[str, list[TableCell], str]] = []
    for row_open, cells, row_close in rows:
        rendered_cells: list[TableCell] = []
        for index, cell in enumerate(cells):
            if ROWSPAN_UP_RE.fullmatch(cell.content):
                anchor = anchors.get(index)
                if anchor is not None:
                    anchor.rowspan += 1
                    continue
            elif COLSPAN_LEFT_RE.fullmatch(cell.content):
                if rendered_cells:
                    rendered_cells[-1].colspan += 1
                    continue
            else:
                anchors[index] = cell

            rendered_cells.append(cell)

        filtered_rows.append((row_open, rendered_cells, row_close))

    active_rowspans: dict[int, int] = {}
    for _, cells, _ in filtered_rows:
        next_col = 1
        new_rowspans: dict[int, int] = {}
        for cell in cells:
            while active_rowspans.get(next_col, 0) > 0:
                next_col += 1

            cell.logical_col = next_col

            if cell.rowspan > 1:
                for col in range(next_col, next_col + cell.colspan):
                    new_rowspans[col] = max(new_rowspans.get(col, 0), cell.rowspan - 1)

            next_col += cell.colspan

        next_active_rowspans = {
            col: remaining - 1
            for col, remaining in active_rowspans.items()
            if remaining > 1
        }
        for col, remaining in new_rowspans.items():
            next_active_rowspans[col] = max(next_active_rowspans.get(col, 0), remaining)
        active_rowspans = next_active_rowspans

    rendered_rows = [
        f"{row_open}{''.join(cell.render() for cell in cells)}{row_close}"
        for row_open, cells, row_close in filtered_rows
    ]

    output: list[str] = []
    for prefix, row_html in zip(row_prefixes, rendered_rows):
        output.append(prefix)
        output.append(row_html)
    output.append(table_html[last_end:])
    return "".join(output)


def on_page_markdown(markdown: str, **kwargs) -> str:
    """Preserve merge markers through Markdown parsing."""

    def _replace(match: re.Match[str]) -> str:
        name = match.group("name").lower()
        if name in {"rowspan-up", "colspan-up"}:
            return ROWSPAN_SENTINEL
        return COLSPAN_LEFT_SENTINEL

    return MERGE_MARKDOWN_RE.sub(_replace, markdown)


def on_page_content(html: str, **kwargs) -> str:
    """Apply optional table classes and vertical table merges."""

    html = _apply_table_classes(html)
    return TABLE_RE.sub(lambda match: _apply_rowspan_markers(match.group(0)), html)
