"""Normalizador HTML a Markdown determinista.

Convierte contenido web en texto limpio / Markdown estructurado para:
1. Eliminar boilerplate, scripts, estilos y ruido visual.
2. Generar extractos citables con trazabilidad.
3. Calcular hashes de contenido limpios sin artefactos de renderizado.
"""

from __future__ import annotations

import html
import re
from html.parser import HTMLParser


class _HTMLToMarkdownParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self._pieces: list[str] = []
        self._ignore_stack: list[str] = []
        self.title: str = ""
        self._in_title: bool = False
        self._ignored_tags = frozenset({"script", "style", "noscript", "svg", "path"})

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag_l = tag.lower()
        if tag_l in self._ignored_tags:
            self._ignore_stack.append(tag_l)
            return

        if tag_l == "title":
            self._in_title = True
        elif tag_l in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            level = int(tag_l[1])
            self._pieces.append(f"\n\n{'#' * level} ")
        elif tag_l in {"p", "div", "section", "article"}:
            self._pieces.append("\n\n")
        elif tag_l == "br":
            self._pieces.append("\n")
        elif tag_l == "li":
            self._pieces.append("\n- ")
        elif tag_l in {"td", "th"}:
            self._pieces.append(" | ")
        elif tag_l == "tr":
            self._pieces.append("\n")

    def handle_endtag(self, tag: str) -> None:
        tag_l = tag.lower()
        if self._ignore_stack and self._ignore_stack[-1] == tag_l:
            self._ignore_stack.pop()
            return

        if tag_l == "title":
            self._in_title = False
        elif tag_l in {"p", "div", "section", "article"}:
            self._pieces.append("\n")

    def handle_data(self, data: str) -> None:
        if self._ignore_stack:
            return
        if self._in_title:
            self.title += data
            return
        self._pieces.append(data)


def normalize_html_to_markdown(raw_html: str) -> tuple[str, str]:
    """Convierte HTML crudo a (title, markdown_text).

    Limpia etiquetas de script/style, resuelve entidades HTML y colapsa saltos excesivos.
    """
    if not isinstance(raw_html, str):
        raise TypeError(f"Se esperaba str, se recibió {type(raw_html).__name__}")

    parser = _HTMLToMarkdownParser()
    parser.feed(raw_html)
    parser.close()

    title = html.unescape(parser.title).strip()
    raw_text = "".join(parser._pieces)
    raw_text = html.unescape(raw_text)

    # Limpieza de espacios y líneas
    lines = [re.sub(r"[ \t]+", " ", line).strip() for line in raw_text.splitlines()]
    clean_text = "\n".join(lines)
    # Colapsar 3 o más saltos de línea consecutivos a 2
    clean_text = re.sub(r"\n{3,}", "\n\n", clean_text).strip()

    if not title:
        # Extraer primer encabezado si no hay <title>
        first_h = re.search(r"^#+\s*(.+)$", clean_text, flags=re.MULTILINE)
        title = first_h.group(1).strip() if first_h else "Sin título"

    return title, clean_text


def extract_excerpt(text: str, max_chars: int = 500) -> str:
    """Extrae un fragmento representativo del texto normalizado."""
    if not text:
        return ""
    clean = re.sub(r"\s+", " ", text).strip()
    if len(clean) <= max_chars:
        return clean
    # Cortar en el límite de la última palabra completa
    truncated = clean[:max_chars]
    last_space = truncated.rfind(" ")
    if last_space > 0:
        truncated = truncated[:last_space]
    return truncated + "..."
