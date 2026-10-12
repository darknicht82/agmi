from src.normalization.html_normalizer import (
    extract_excerpt,
    normalize_html_to_markdown,
)


def test_normalize_html_basic() -> None:
    raw_html = """
    <!DOCTYPE html>
    <html>
      <head>
        <title>Oferta de Empleo: Desarrollador Python en Quito</title>
        <script>console.log("tracker");</script>
        <style>.btn { color: red; }</style>
      </head>
      <body>
        <header>Navegación</header>
        <h1>Búsqueda de Profesional</h1>
        <p>Se requiere integrar <b>APIs de pagos</b> y facturación local.</p>
        <ul>
          <li>Experiencia en Python</li>
          <li>Conocimiento de normativa local</li>
        </ul>
        <footer>Derechos reservados 2026</footer>
      </body>
    </html>
    """
    title, markdown = normalize_html_to_markdown(raw_html)

    assert title == "Oferta de Empleo: Desarrollador Python en Quito"
    assert "tracker" not in markdown
    assert "color: red" not in markdown
    assert "Se requiere integrar APIs de pagos" in markdown
    assert "- Experiencia en Python" in markdown


def test_extract_excerpt() -> None:
    text = "Problema con inventario: empresa pierde horas cuadrando cajas manualmente."
    excerpt = extract_excerpt(text, max_chars=40)
    assert len(excerpt) <= 45
    assert excerpt.endswith("...")
    assert "Problema" in excerpt
