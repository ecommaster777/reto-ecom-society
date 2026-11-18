#!/usr/bin/env python3
"""Exporta las 7 piezas del carrusel a imagen, al doble de resolución (2160 x 2160).

Uso:  python3 exportar_galeria.py carpeta_salida
Lee carpeta_salida/galeria.html y deja carpeta_salida/fotos/galeria-1.png ... galeria-7.png
Necesita Google Chrome instalado.
"""
import os, sys, shutil, subprocess, platform
from pathlib import Path

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

def main():
    out = Path(sys.argv[1]).resolve()
    g = out / "galeria.html"; (out / "fotos").mkdir(exist_ok=True)
    c = chrome()
    for n in range(1, 8):
        destino = out / "fotos" / f"galeria-{n}.png"
        subprocess.run([c, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=2",
                        "--window-size=1080,1080", "--virtual-time-budget=12000", "--run-all-compositor-stages-before-draw",
                        f"--screenshot={destino}", g.as_uri() + f"#{n}"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=90)
        print("Pieza", n, "→", destino)

if __name__ == "__main__":
    main()
