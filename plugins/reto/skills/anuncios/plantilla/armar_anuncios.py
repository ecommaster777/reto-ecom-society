#!/usr/bin/env python3
"""Arma los anuncios del reto a partir de campana.json.

Uso:  python3 armar_anuncios.py anuncios/campana.json
Las rutas de fotos y videos dentro de campana.json son relativas a la carpeta del json (por ejemplo anuncios/).

Deja en esa carpeta:
  imagenes/<ID>.png   cada anuncio de imagen, 1080 x 1350, listo para subir a Meta
  revision.html       los anuncios como se ven en el celular, con sus textos, para aprobarlos
  campana.md          la guía para montar la campaña a mano en el Administrador de anuncios
Necesita Google Chrome instalado.
"""
import json, sys, os, shutil, subprocess, platform, html
from pathlib import Path
from urllib.parse import quote

AQUI = Path(__file__).resolve().parent
PLANTILLAS = {"nota": ["titulo", "lineas"], "post": ["texto"], "ugc": ["foto", "burbujas"], "beneficios": ["titulo", "puntos", "pie"],
              "oferta": ["titulo", "precio"], "bloqueo": ["fondo", "hora", "notificaciones"], "calendario": ["mes", "dias"], "editorial": ["foto", "titulo"], "comparacion": ["titulo", "nuestro", "otro", "nombre_otro", "foto_otro"]}
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

def chrome():
    candidatos = {
        "Darwin": ["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"],
        "Windows": [r"C:\Program Files\Google\Chrome\Application\chrome.exe", r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
                    os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe")],
    }.get(platform.system(), []) + [shutil.which("google-chrome") or "", shutil.which("chromium") or ""]
    for c in candidatos:
        if c and Path(c).exists():
            return c
    sys.exit("No encontré Google Chrome. Instálalo y vuelve a correr este paso.")

def fuentes(m):
    extra = '<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Caveat:wght@700&display=block" rel="stylesheet">'
    fams = "&".join("family=" + quote(f).replace("%20", "+") + ":wght@400;500;600;700;800" for f in dict.fromkeys(m["fuentes"].values()))
    return extra + f'<link href="https://fonts.googleapis.com/css2?{fams}&display=block" rel="stylesheet">'

PARAMS = "utm_source=meta&utm_medium=paid&utm_campaign=reto&utm_content={{ad.name}}"

def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    cj = Path(sys.argv[1]).resolve(); out = cj.parent
    if not cj.exists():
        sys.exit(f"No encontré {cj}")
    try:
        C = json.loads(cj.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        sys.exit(f"campana.json tiene un error de escritura en la línea {e.lineno}: {e.msg}")
    if not isinstance(C, dict):
        sys.exit("campana.json tiene que empezar con { y ser un objeto, no una lista.")
    req = [k for k in ("nombre_campana", "url", "moneda", "presupuesto_diario", "cpa_max", "paises", "marca", "conjuntos") if k not in C]
    if "paises" in C and not isinstance(C["paises"], list): req.append('"paises" tiene que ser una lista, por ejemplo ["México", "Chile"]')
    if not isinstance(C.get("conjuntos", []), list): req.append('"conjuntos" tiene que ser una lista')
    m_ = C.get("marca", {}) if isinstance(C.get("marca"), dict) else {}
    if not isinstance(m_.get("colores", {}), dict) or "principal" not in m_.get("colores", {}): req.append("marca.colores.principal")
    if not isinstance(m_.get("fuentes", {}), dict) or not {"titulos", "textos"} <= set(m_.get("fuentes", {})): req.append("marca.fuentes con titulos y textos")
    for c in C.get("conjuntos", []) if isinstance(C.get("conjuntos"), list) else []:
        for k in ("nombre", "angulo"):
            if not isinstance(c.get(k), str): req.append(f'un conjunto no tiene "{k}" (texto)')
        for a in c.get("anuncios", []):
            for k in ("id", "formato", "texto_principal", "titulo"):
                if k in a and not isinstance(a[k], str): req.append(f'anuncio {a.get("id")}: "{k}" tiene que ser texto (entre comillas)')
    req += [f"marca.{k}" for k in ("nombre", "logo", "colores", "fuentes") if k not in C.get("marca", {})]
    ids = [a.get("id") for c in C.get("conjuntos", []) for a in c.get("anuncios", [])]
    req += [f'anuncio {a.get("id", "?")}: {k}' for c in C.get("conjuntos", []) for a in c.get("anuncios", []) for k in ("id", "formato", "texto_principal", "titulo") if not a.get(k)]
    if len(ids) != len(set(ids)):
        req.append("hay IDs de anuncio repetidos: " + ", ".join(sorted({i for i in ids if ids.count(i) > 1})))
    if req:
        sys.exit("En campana.json falta o está mal:\n  " + "\n  ".join(req))
    for c in C["conjuntos"]:
        for a in c["anuncios"]:
            if len(a["titulo"]) > 40: print(f'Ojo: el título de {a["id"]} tiene {len(a["titulo"])} caracteres (máximo 40): Meta lo va a cortar.')
            if len(a.get("descripcion", "")) > 30: print(f'Ojo: la descripción de {a["id"]} tiene {len(a["descripcion"])} caracteres (máximo 30).')
    for f in ("piezas.css", "piezas.js"):
        shutil.copy(AQUI / f, out / f)
    datos = json.dumps(C, ensure_ascii=False)
    (out / "piezas.html").write_text(f'''<!doctype html><html lang="es"><head><meta charset="utf-8">{fuentes(C["marca"])}
<link rel="stylesheet" href="piezas.css"></head><body><script>window.CAMPANA={datos};</script><script src="piezas.js"></script>
<script>window.addEventListener("hashchange",()=>location.reload())</script></body></html>''', encoding="utf-8")

    # 1. Las imágenes
    (out / "imagenes").mkdir(exist_ok=True)
    c = chrome(); faltan = []; errores = []
    for k in ("logo", "logo_claro", "producto_sin_fondo"):
        if C["marca"].get(k) and not (out / C["marca"][k]).exists():
            faltan.append(C["marca"][k])
    for cjto in C["conjuntos"]:
        for ad in cjto["anuncios"]:
            if ad.get("pieza"):
                viejo = out / "imagenes" / f'{ad["id"]}.png'
                if viejo.exists(): viejo.unlink()
                pl = ad["pieza"].get("plantilla")
                if pl not in PLANTILLAS:
                    ad["archivo"] = ""
                    errores.append(f'{ad["id"]}: la plantilla "{pl}" no existe (usa {", ".join(sorted(PLANTILLAS))})'); continue
                LISTAS = ("lineas", "burbujas", "puntos", "nuestro", "otro", "notificaciones", "dias")
                falta = [k for k in PLANTILLAS[pl] if not ad["pieza"].get(k)] + [f"{k} (tiene que ser una lista)" for k in LISTAS if k in ad["pieza"] and not isinstance(ad["pieza"][k], list)]
                if falta:
                    ad["archivo"] = ""
                    errores.append(f'{ad["id"]}: a la pieza "{pl}" le falta {", ".join(falta)}'); continue
                for k in ("foto", "foto_otro", "fondo"):
                    if ad["pieza"].get(k) and not (out / ad["pieza"][k]).exists():
                        faltan.append(ad["pieza"][k])
                destino = out / "imagenes" / f'{ad["id"]}.png'
                if destino.exists(): destino.unlink()
                subprocess.run([c, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--window-size=1080,1350",
                                "--virtual-time-budget=12000", "--run-all-compositor-stages-before-draw",
                                f"--screenshot={destino}", (out / "piezas.html").as_uri() + "#" + ad["id"]],
                               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=120)
                if not destino.exists():
                    errores.append(f'{ad["id"]}: Chrome no pudo hacer la imagen')
                ad["archivo"] = f'imagenes/{ad["id"]}.png'
                print("Imagen", ad["id"], "→", destino)
            elif ad.get("video"):
                ad["archivo"] = ad["video"]
                if not (out / ad["video"]).exists():
                    faltan.append(ad["video"])
            else:
                ad["archivo"] = ""
                errores.append(f'{ad["id"]}: no tiene "pieza" ni "video"')
    if faltan or errores:
        print("\nHay que corregir esto antes de seguir:", *sorted(set(faltan)), *errores, sep="\n  ")

    if faltan or errores:
        sys.exit(1)

    # 2. La revisión en el celular
    m = C["marca"]; e = html.escape
    def tarjeta(ad):
        medio = (f'<video src="{ad["archivo"]}" controls playsinline loop muted></video>' if ad.get("video")
                 else f'<img src="{ad["archivo"]}">')
        return f'''<div class="ad"><div class="tag">{e(ad["id"])} · {e(ad["formato"])}</div><div class="phone">
<div class="hd"><img src="{e(m.get("logo_claro") or m["logo"])}"><div><b>{e(m["nombre"])}</b><small>Publicidad</small></div></div>
<p class="tp">{e(ad["texto_principal"])}</p>{medio}
<div class="ft"><div><small>{e(C.get("dominio",""))}</small><b>{e(ad["titulo"])}</b><span>{e(ad.get("descripcion",""))}</span></div><a>{e(C.get("boton","Comprar"))}</a></div></div></div>'''
    secs = "".join(f'''<section><h2>{e(c["nombre"])}</h2><p class="ang">{e(c["angulo"])}</p><p class="pq">{e(c.get("por_que",""))}</p>
<div class="grid">{"".join(tarjeta(a) for a in c["anuncios"])}</div></section>''' for c in C["conjuntos"])
    (out / "revision.html").write_text(f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Anuncios · {e(m["nombre"])}</title><style>
body{{margin:0;background:#f0f2f5;font:15px/1.4 -apple-system,system-ui,sans-serif;color:#1c1e21}}
header{{background:{m["colores"]["principal"]};color:#fff;padding:28px 24px}}header h1{{margin:0;font-size:26px}}header p{{margin:6px 0 0;opacity:.85}}
section{{padding:26px 24px}}h2{{margin:0 0 4px;font-size:22px}}.ang{{margin:0;font-weight:600}}.pq{{margin:4px 0 16px;color:#65676b}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:18px}}
.tag{{font:700 12px system-ui;letter-spacing:.06em;text-transform:uppercase;color:#65676b;margin-bottom:6px}}
.phone{{background:#fff;border-radius:12px;box-shadow:0 1px 3px #0002;overflow:hidden}}
.hd{{display:flex;gap:10px;align-items:center;padding:12px}}.hd img{{width:38px;height:38px;border-radius:50%;object-fit:contain;background:{m["colores"]["principal"]};padding:5px}}
.hd b{{display:block}}.hd small{{color:#65676b}}.tp{{margin:0;padding:0 12px 10px;white-space:pre-line}}
.phone img:not(.hd img),.phone video{{width:100%;display:block;background:#000}}
.ft{{display:flex;justify-content:space-between;align-items:center;gap:10px;background:#f0f2f5;padding:10px 12px}}
.ft small{{display:block;color:#65676b;text-transform:uppercase;font-size:11px}}.ft b{{display:block}}.ft span{{color:#65676b;font-size:13px}}
.ft a{{background:#e4e6eb;border-radius:6px;padding:8px 12px;font-weight:600;white-space:nowrap}}
</style></head><body><header><h1>Tus anuncios · {e(m["nombre"])}</h1><p>{len(C["conjuntos"])} conjuntos · {sum(len(c["anuncios"]) for c in C["conjuntos"])} anuncios · revísalos en el celular y aprueba</p></header>{secs}</body></html>''', encoding="utf-8")

    # 3. La guía para montarla a mano
    g = [f'# Tu campaña · {m["nombre"]}', "", "Móntala en https://adsmanager.facebook.com siguiendo este orden. Copia y pega cada texto tal cual.", "",
         "## 1. La campaña", "- Botón verde **+ Crear** › objetivo **Ventas** › Continuar.",
         f'- Nombre: **{C["nombre_campana"]}**',
         f'- Presupuesto **de la campaña** (Advantage+): **{C["moneda"]} {C["presupuesto_diario"]} al día**. Meta lo reparte entre los {len(C["conjuntos"])} conjuntos.',
         "- Estrategia de puja: volumen más alto (la que viene por defecto).", ""]
    for i, cjto in enumerate(C["conjuntos"], 1):
        g += [f'## {i + 1}. Conjunto {i} · {cjto["nombre"]}',
              f'- Nombre del conjunto: **{cjto["nombre"]}**',
              "- Conversión: **Sitio web**, tu píxel (Meta ahora lo llama **conjunto de datos**; lo creó la app de Facebook e Instagram de Shopify), evento **Compra**.",
              f'- Ubicación (países): **{", ".join(C["paises"])}**',
              f'- Idioma: **{C.get("idioma_publico", "Todos")}**',
              f'- Público: **Advantage+**, sin intereses. Edad mínima en los controles: 25 (la edad de tu cliente, {C.get("edad", "30 a 65+")}, va como sugerencia).',
              "- Ubicaciones: **Advantage+** (automáticas).", "", "### Los anuncios de este conjunto",
              "En cada anuncio: elige **tu página de Facebook y tu cuenta de Instagram**. Después busca **Mejoras de Advantage+ creative** y apaga una por una: mejoras de texto, retoques visuales (brillo y contraste), superposiciones e información de la tienda, expandir imagen, generar fondo, música, animación, traducción, enlaces del sitio, agregar productos del catálogo, comentarios relevantes y anuncios de varios anunciantes. Pueden cambiar tu texto o tu imagen y romper las reglas de salud."]
        for ad in cjto["anuncios"]:
            g += [f'**Anuncio {ad["id"]} · {ad["formato"]}**', f'- Nombre: `{ad["id"]} · {ad["formato"]}`', f'- Archivo: `{ad["archivo"]}`',
                  "- Texto principal:", "", "```", ad["texto_principal"], "```", "",
                  f'- Título: `{ad["titulo"]}`', f'- Descripción: `{ad.get("descripcion","")}`',
                  f'- Llamado a la acción: **{C.get("boton","Comprar")}**', f'- URL del sitio web: `{C["url"]}`',
                  f'- Parámetros de URL (abajo, en "Seguimiento"): `{PARAMS}`', ""]
        if i < len(C["conjuntos"]):
            g += [f'Para el conjunto {i + 1}: en la columna de la izquierda, sobre el conjunto {i} ya armado, los 3 puntos › **Duplicar** › en la misma campaña. Cámbiale el nombre y, en cada anuncio, cambia archivo, textos y nombre por los de abajo.', ""]
    g += ["## Si algo no aparece",
          "- **El evento Compra sale restringido** (Meta a veces limita las tiendas de salud, sobre todo en Estados Unidos): saca Estados Unidos del conjunto o lleva la captura al grupo del reto.",
          "- **Meta no te deja duplicar el conjunto:** crea la campaña otra vez eligiendo la configuración manual en vez de la de Advantage+.", "",
          "## Antes de publicar", "- Revisa que cada anuncio tenga su archivo, sus textos y su URL.",
          "- Clic en **Publicar**. Meta revisa los anuncios (de minutos a unas horas).", "",
          "## Las reglas hasta el domingo",
          "- **No toques nada.** Ni presupuesto, ni anuncios, ni públicos. Meta necesita esos días para aprender.",
          f'- Tu número para el domingo: puedes pagar hasta **{C["moneda"]} {C["cpa_max"]}** por venta.']
    (out / "campana.md").write_text("\n".join(g) + "\n", encoding="utf-8")
    # La misma guía en HTML, para leerla cómoda en el navegador
    import re as _re
    def md(l):
        l = html.escape(l); l = _re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", l); l = _re.sub(r"`(.+?)`", r"<code>\1</code>", l)
        return _re.sub(r"(https://[^\s<]+)", r'<a href="\1" target="_blank">\1</a>', l)
    body, pre = [], False
    for l in g:
        if l.startswith("```"):
            body.append("</pre>" if pre else "<pre>"); pre = not pre; continue
        if pre: body.append(html.escape(l)); continue
        if l.startswith("### "): body.append(f"<h3>{md(l[4:])}</h3>")
        elif l.startswith("## "): body.append(f"<h2>{md(l[3:])}</h2>")
        elif l.startswith("# "): body.append(f"<h1>{md(l[2:])}</h1>")
        elif l.startswith("- "): body.append(f"<li>{md(l[2:])}</li>")
        elif l: body.append(f"<p>{md(l)}</p>")
    (out / "campana.html").write_text(f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Tu campaña</title>
<style>body{{max-width:820px;margin:0 auto;padding:24px;font:17px/1.55 -apple-system,system-ui,sans-serif;color:#1c1e21}}h2{{margin-top:34px;padding-top:14px;border-top:2px solid #e4e6eb}}
h3{{color:#555}}li{{margin:4px 0 4px 18px}}code{{background:#f0f2f5;padding:2px 6px;border-radius:5px}}pre{{background:#f0f2f5;padding:14px;border-radius:10px;white-space:pre-wrap;font:16px/1.5 -apple-system,system-ui,sans-serif}}</style></head><body>{"".join(body)}</body></html>''', encoding="utf-8")
    json.dump(C, open(cj, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    if faltan or errores:
        sys.exit(1)
    print("\nListo:", out / "revision.html", "y", out / "campana.html")

if __name__ == "__main__":
    main()
