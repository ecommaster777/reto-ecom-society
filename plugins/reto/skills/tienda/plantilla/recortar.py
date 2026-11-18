#!/usr/bin/env python3
"""Recorta el espacio vacío (transparente) alrededor de un PNG: el logo y el frasco sin fondo.

Higgsfield entrega las imágenes sin fondo en un cuadro de 1024 x 1024 con mucho espacio
alrededor; sin recortar, el logo se ve diminuto en la página.

Uso:  python3 recortar.py fotos/logo.png fotos/frasco.png
Necesita Pillow. Si no está, este script te dice cómo instalarlo.
"""
import sys

try:
    from PIL import Image
except ImportError:
    sys.exit(
        "Falta Pillow. Instálalo una sola vez y vuelve a correr este comando con el Python del entorno:\n"
        "  Mac:     python3 -m venv ~/.reto-py && ~/.reto-py/bin/pip install pillow\n"
        "           ~/.reto-py/bin/python recortar.py ...\n"
        "  Windows: py -m venv %USERPROFILE%\\.reto-py && %USERPROFILE%\\.reto-py\\Scripts\\pip install pillow\n"
        "           %USERPROFILE%\\.reto-py\\Scripts\\python recortar.py ..."
    )

if len(sys.argv) < 2:
    sys.exit(__doc__)

for ruta in sys.argv[1:]:
    im = Image.open(ruta).convert("RGBA")
    caja = im.getchannel("A").point(lambda a: 255 if a > 20 else 0).getbbox()
    if not caja:
        print(f"{ruta}: no tiene fondo transparente, quítale el fondo primero")
        continue
    x0, y0, x1, y1 = caja
    m = max(4, int(0.02 * max(x1 - x0, y1 - y0)))  # un margen pequeño
    caja = (max(0, x0 - m), max(0, y0 - m), min(im.width, x1 + m), min(im.height, y1 + m))
    im.crop(caja).save(ruta)
    print(f"{ruta}: {im.size[0]}x{im.size[1]} -> {caja[2]-caja[0]}x{caja[3]-caja[1]}")
