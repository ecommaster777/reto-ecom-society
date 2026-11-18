#!/usr/bin/env python3
"""Arma la página de producto y el carrusel a partir de la plantilla del Reto.

Uso:
  python3 armar.py datos.json carpeta_salida
Deja en carpeta_salida:
  index.html     la página de producto (prototipo)
  galeria.html   las 7 piezas del carrusel (para exportarlas con exportar_galeria.py)
Las rutas de las imágenes en datos.json son relativas a carpeta_salida (fotos/...).

Con un tercer argumento (la carpeta del tema bajado con `shopify theme pull`) además copia la plantilla
al tema: sections/pdp-reto.liquid, snippets/pdp-reto-datos.liquid, layout/reto.liquid,
templates/product.reto.json y assets/pdp-reto.css y .js.
"""
import json, sys, urllib.parse
from pathlib import Path

AQUI = Path(__file__).parent

def fuentes(d):
    f = d["marca"]["fuentes"]
    fam = lambda n, w: "family=" + urllib.parse.quote_plus(n) + ":wght@" + w
    return f'https://fonts.googleapis.com/css2?{fam(f["titulos"], "600;800")}&{fam(f["textos"], "400;500;700")}&display=block'

def pagina(d, css, js, raiz, llamada, extra_css=""):
    return f"""<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{d.get("nombre_producto", d["marca"]["nombre"])}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{fuentes(d)}" rel="stylesheet">
<style>html,body{{margin:0}}{extra_css}{css}</style></head>
<body><div id="{raiz}"></div>
<script id="datos" type="application/json">{json.dumps(d, ensure_ascii=False)}</script>
<script>{js}</script>
<script>{llamada}</script>
</body></html>"""

def main():
    if len(sys.argv) not in (3, 4):
        sys.exit("Uso: python3 armar.py datos.json carpeta_salida [carpeta_del_tema_de_shopify]")
    d = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    out = Path(sys.argv[2]); out.mkdir(parents=True, exist_ok=True)
    leer = lambda n: (AQUI / n).read_text(encoding="utf-8")
    datos_js = "JSON.parse(document.getElementById('datos').textContent)"
    (out / "index.html").write_text(pagina(d, leer("pdp-reto.css"), leer("pdp-reto.js"), "pdp",
        f"PDPReto.render(document.getElementById('pdp'), {datos_js});"), encoding="utf-8")
    if "carrusel" in d:
        (out / "galeria.html").write_text(pagina(d, leer("galeria-reto.css"), leer("galeria-reto.js"), "gal",
            f"document.fonts.ready.then(()=>0);GaleriaReto.render(document.getElementById('gal'), {datos_js});"), encoding="utf-8")
    print("Listo:", out / "index.html", "y", out / "galeria.html" if "carrusel" in d else "")

if __name__ == "__main__":
    main()


# ---------- Shopify ----------
LIQUID_SECCION = """{%- comment -%} Página de producto del Reto. No editar: el contenido está en snippets/pdp-reto-datos.liquid {%- endcomment -%}
{{ 'pdp-reto.css' | asset_url | stylesheet_tag }}
<div id="pdp"></div>
<script id="datos" type="application/json">{% render 'pdp-reto-datos' %}</script>
<script>
window.PDP_VARIANTES=[{%- for v in product.variants -%}{"id":{{ v.id }},"p":{{ v.price }},"c":{{ v.compare_at_price | default: 0 }}}{%- unless forloop.last -%},{%- endunless -%}{%- endfor -%}];
window.PDP_MONEDA={{ cart.currency.iso_code | json }};
</script>
<script src="{{ 'pdp-reto.js' | asset_url }}" defer></script>
<script>
document.addEventListener('DOMContentLoaded',function(){
 var d=JSON.parse(document.getElementById('datos').textContent),f=d.marca.fuentes;
 var q=function(n,w){return 'family='+encodeURIComponent(n).replace(/%20/g,'+')+':wght@'+w};
 var l=document.createElement('link');l.rel='stylesheet';l.href='https://fonts.googleapis.com/css2?'+q(f.titulos,'600;800')+'&'+q(f.textos,'400;500;700')+'&display=swap';document.head.appendChild(l);
 PDPReto.render(document.getElementById('pdp'),d,{variantes:window.PDP_VARIANTES,moneda:window.PDP_MONEDA});
});
</script>
{% schema %}
{"name":"Página del Reto","settings":[]}
{% endschema %}
"""
LIQUID_LAYOUT = """<!doctype html>
<html lang="{{ request.locale.iso_code }}">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{{ page_title }}{% unless page_title contains shop.name %} | {{ shop.name }}{% endunless %}</title>
{% if page_description %}<meta name="description" content="{{ page_description | escape }}">{% endif %}
<link rel="canonical" href="{{ canonical_url }}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<style>html,body{margin:0}</style>
{{ content_for_header }}
</head>
<body>
{{ content_for_layout }}
</body>
</html>
"""
TEMPLATE_JSON = {"layout": "reto", "sections": {"main": {"type": "pdp-reto", "settings": {}}}, "order": ["main"]}

def a_shopify(d, tema, fotos=None):
    """Copia la plantilla a la carpeta del tema de Shopify y convierte las rutas fotos/x en {{ 'x' | asset_url }}."""
    import shutil, re
    tema = Path(tema)
    for sub in ("sections", "snippets", "templates", "layout", "assets"):
        (tema / sub).mkdir(parents=True, exist_ok=True)
    shutil.copy(AQUI / "pdp-reto.css", tema / "assets" / "pdp-reto.css")
    shutil.copy(AQUI / "pdp-reto.js", tema / "assets" / "pdp-reto.js")
    (tema / "sections" / "pdp-reto.liquid").write_text(LIQUID_SECCION, encoding="utf-8")
    (tema / "layout" / "reto.liquid").write_text(LIQUID_LAYOUT, encoding="utf-8")
    (tema / "templates" / "product.reto.json").write_text(json.dumps(TEMPLATE_JSON, indent=1), encoding="utf-8")
    txt = json.dumps({k: v for k, v in d.items() if k != "carrusel"}, ensure_ascii=False, indent=1)
    usadas = sorted(set(re.findall(r'"fotos/([^"]+)"', txt)))
    txt = re.sub(r'"fotos/([^"]+)"', lambda m: '"{{ \'' + m.group(1) + '\' | asset_url }}"', txt)
    doc = "{%- doc -%}\nDatos de la página del Reto en JSON. Se edita desde datos.json y armar.py.\n@example\n{% render 'pdp-reto-datos' %}\n{%- enddoc -%}"
    (tema / "snippets" / "pdp-reto-datos.liquid").write_text(doc + txt, encoding="utf-8")
    if fotos and Path(fotos).is_dir():
        for n in usadas:
            if (Path(fotos) / n).exists():
                shutil.copy(Path(fotos) / n, tema / "assets" / n)
    faltan = [n for n in usadas if not (tema / "assets" / n).exists()]
    return faltan

if __name__ == "__main__" and len(sys.argv) == 4:
    d = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    faltan = a_shopify(d, sys.argv[3], Path(sys.argv[2]) / "fotos")
    print("Tema listo en", sys.argv[3] + (" · FALTAN en assets/: " + ", ".join(faltan) if faltan else " · todas las imágenes copiadas a assets/"))
