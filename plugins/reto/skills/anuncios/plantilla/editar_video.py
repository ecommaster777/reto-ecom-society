#!/usr/bin/env python3
"""Edita los videos de los anuncios: recorta, pone títulos y subtítulos en la zona segura de Reels
y deja cada video en 1080 x 1920, listo para Meta.

Uso:
  python3 editar_video.py anuncios/campana.json        edita todos los videos que tengan "edicion"
  python3 editar_video.py --transcribir video.mp4      escribe lo que dice la persona, palabra por palabra con su segundo
                                                       (necesita: python3 -m pip install --user faster-whisper)
  python3 editar_video.py --pausas video.mp4           si no hay faster-whisper: muestra en qué tramos habla la persona

En campana.json, cada anuncio de video lleva:
  "original": "videos/originales/1E.mp4",   el video como salió de Higgsfield
  "video": "videos/1E.mp4",                 dónde queda el editado
  "edicion": {
    "recorte": [0.3, 14.6],                 opcional: segundo de inicio y de fin
    "anexar": {"video": "videos/originales/X.mp4", "desde": 5, "hasta": 8},   opcional: pega al final un segundo clip (por ejemplo, el producto de día)
    "aviso_ia": true,                       si aparece una persona hecha con IA (pone "Video creado con IA")
    "extender": 2,                          opcional: segundos de cuadro congelado al final, para el cierre
    "textos": [ {"t0": 0, "t1": 2.4, "texto": "…", "zona": "arriba", "estilo": "titulo"} , … ],
    "cierre": {"t0": 6.4, "texto": "Envío gratis · 30 días de garantía", "zona": "abajo", "sin_logo": false}
                                            sin_logo: true si el producto ya se ve grande en ese momento (así no tapas la etiqueta)
  }
zona: arriba | centro | abajo (siempre dentro de la zona segura). alinear (opcional): derecha | izquierda, para dejar libre el producto o la cara del otro lado. estilo: titulo (caja blanca grande) | subtitulo (caja blanca más chica).
Si en el segundo del cierre el producto está en el centro, usa "zona": "arriba" y "sin_logo": true para no tapar la etiqueta.
Regla: los subtítulos nunca tapan la cara. Mira un cuadro del video y elige la zona donde no hay rostro.
Necesita Google Chrome y ffmpeg.
"""
import json, sys, os, re, shutil, subprocess, platform, tempfile, html
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

W, H = 1080, 1920
SEG_ARRIBA, SEG_ABAJO, LADO = 310, 1230, 80      # Reels: libre el 14 % de arriba y el 35 % de abajo

def chrome():
    for c in {"Darwin": ["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"],
              "Windows": [r"C:\Program Files\Google\Chrome\Application\chrome.exe", r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
                          os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe")]}.get(platform.system(), []) + [shutil.which("google-chrome") or "", shutil.which("chromium") or ""]:
        if c and Path(c).exists():
            return c
    sys.exit("No encontré Google Chrome.")

def ffmpeg():
    f = shutil.which("ffmpeg")
    if not f:
        sys.exit("Falta ffmpeg. En Mac: brew install ffmpeg · En Windows: winget install Gyan.FFmpeg (y vuelve a abrir la terminal).")
    return f

CSS = f"""*{{margin:0;padding:0;box-sizing:border-box}}html,body{{width:{W}px;height:{H}px;background:transparent;overflow:hidden}}
.z{{position:absolute;left:{LADO}px;right:{LADO}px;display:flex;flex-direction:column;align-items:center;gap:8px;text-align:center}}
.der{{align-items:flex-end;text-align:right}}.izq{{align-items:flex-start;text-align:left}}
.arriba{{top:{SEG_ARRIBA}px}}.abajo{{bottom:{H - SEG_ABAJO}px}}.centro{{top:50%;transform:translateY(-50%)}}
.titulo span{{background:#fff;color:#111;font:800 70px/1.15 -apple-system,"Helvetica Neue",Arial,sans-serif;padding:12px 26px;border-radius:16px;box-shadow:0 6px 24px #0004}}
.subtitulo span{{background:#fff;color:#111;font:800 56px/1.15 -apple-system,"Helvetica Neue",Arial,sans-serif;padding:8px 20px;border-radius:12px;box-shadow:0 6px 20px #0005}}
.cierre .card{{background:VAR_COLOR;border-radius:34px;padding:34px 48px 38px;display:flex;flex-direction:column;align-items:center;gap:18px;box-shadow:0 14px 40px #0006}}
.ia{{position:absolute;top:{SEG_ARRIBA}px;left:{LADO}px;background:#0008;color:#fff;font:600 26px -apple-system,"Helvetica Neue",Arial,sans-serif;padding:8px 16px;border-radius:10px}}
.cierre img{{height:96px}}.cierre span{{color:#fff;font:800 50px/1.2 -apple-system,"Helvetica Neue",Arial,sans-serif}}"""

def lineas(t, n=24):
    """Parte el texto en renglones cortos (máximo ~24 letras) para que se lea de un vistazo."""
    out, cur = [], ""
    for w in t.split():
        if cur and len(cur) + 1 + len(w) > n:
            out.append(cur); cur = w
        else:
            cur = (cur + " " + w).strip()
    return out + ([cur] if cur else [])

def capa(chr_, html_txt, destino, color):
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as f:
        f.write(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS.replace("VAR_COLOR", color)}</style></head><body>{html_txt}</body></html>')
        tmp = f.name
    subprocess.run([chr_, "--headless=new", "--disable-gpu", "--hide-scrollbars", f"--window-size={W},{H}", "--default-background-color=00000000",
                    f"--screenshot={destino}", Path(tmp).as_uri()], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=60)
    os.unlink(tmp)

def pausas(video):
    if not Path(video).exists():
        print(f"No encontré {video}"); return
    if "Audio" not in subprocess.run([ffmpeg(), "-i", video], capture_output=True, text=True).stderr:
        print("Este video no tiene audio."); return
    r = subprocess.run([ffmpeg(), "-i", video, "-af", "silencedetect=noise=-32dB:d=0.25", "-f", "null", "-"], capture_output=True, text=True)
    dur = float(re.search(r"Duration: (\d+):(\d+):([\d.]+)", r.stderr).groups()[2]) + 60 * int(re.search(r"Duration: (\d+):(\d+)", r.stderr).group(2))
    ini = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", r.stderr)]
    fin = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", r.stderr)]
    habla, t = [], 0.0
    for a, b in zip(ini, fin + [dur]):
        if a - t > 0.15: habla.append((round(t, 2), round(a, 2)))
        t = b
    if dur - t > 0.15: habla.append((round(t, 2), round(dur, 2)))
    print(f"Duración: {dur:.2f} s. La persona habla en estos tramos (segundos):")
    for a, b in habla: print(f"  {a:6.2f} → {b:6.2f}")

ZONAS, ESTILOS = {"arriba", "centro", "abajo"}, {"titulo", "subtitulo"}

def editar(cj):
    cj = Path(cj).resolve(); base = cj.parent
    try:
        C = json.loads(cj.read_text(encoding="utf-8"))
    except FileNotFoundError:
        sys.exit(f"No encontré {cj}")
    except json.JSONDecodeError as e:
        sys.exit(f"campana.json tiene un error de escritura en la línea {e.lineno}: {e.msg}")
    fallas = []
    ch, ff = chrome(), ffmpeg(); color = C["marca"]["colores"]["principal"]
    logo = C["marca"].get("logo_claro") or C["marca"]["logo"]
    if not (base / logo).exists():
        sys.exit(f"No encontré el logo: {base / logo}")
    for cjto in C["conjuntos"]:
        for ad in cjto["anuncios"]:
            ed = ad.get("edicion")
            if not ed: continue
            if not ad.get("video"):
                fallas.append(f'{ad["id"]}: tiene "edicion" pero le falta "video" (dónde queda el editado)'); continue
            if not isinstance(ed.get("textos", []), list) or (ed.get("recorte") and (not isinstance(ed["recorte"], list) or len(ed["recorte"]) != 2)):
                fallas.append(f'{ad["id"]}: "textos" tiene que ser una lista y "recorte" dos números [inicio, fin]'); continue
            nums = [t.get(k) for t in ed.get("textos", []) for k in ("t0", "t1") if k in t] + ([ed["cierre"].get("t0")] if ed.get("cierre") else []) + (ed.get("recorte") or [])
            if any(not isinstance(n, (int, float)) for n in nums if n is not None):
                fallas.append(f'{ad["id"]}: t0, t1 y recorte van como números, sin comillas (2.5, no "2.5")'); continue
            src = base / ad.get("original", ""); dst = base / ad["video"]; dst.parent.mkdir(parents=True, exist_ok=True)
            if not ad.get("original") or not src.exists():
                fallas.append(f'{ad["id"]}: no encontré el video original ({ad.get("original")}). Bájalo a videos/originales/.'); continue
            if src.resolve() == dst.resolve():
                fallas.append(f'{ad["id"]}: "original" y "video" no pueden ser el mismo archivo.'); continue
            mal = [f'texto {i + 1}' for i, t in enumerate(ed.get("textos", [])) if "t0" not in t or not t.get("texto")
                   or t.get("zona", "abajo") not in ZONAS or t.get("estilo", "subtitulo") not in ESTILOS]
            if ed.get("cierre") and (ed["cierre"].get("zona", "abajo") not in ZONAS or not ed["cierre"].get("texto") or "t0" not in ed["cierre"]):
                mal.append("cierre")
            if mal:
                fallas.append(f'{ad["id"]}: revisa {", ".join(mal)} (cada texto lleva t0, texto, zona arriba/centro/abajo y estilo titulo/subtitulo)'); continue
            tmpd = Path(tempfile.mkdtemp()); capas = []
            r0, r1 = ed.get("recorte", [0, None])
            for i, t in enumerate(ed.get("textos", [])):
                lado = {"derecha": "der", "izquierda": "izq"}.get(t.get("alinear", ""), "")
                ancho = (22 if t.get("estilo") == "titulo" else 24) - (6 if lado else 0)
                spans = "".join(f"<span>{html.escape(l)}</span>" for l in lineas(t["texto"], ancho))
                p = tmpd / f"t{i}.png"; capa(ch, f'<div class="z {t.get("zona","abajo")} {t.get("estilo","subtitulo")} {lado}">{spans}</div>', p, color)
                capas.append((p, t["t0"], t.get("t1", t["t0"] + 2.5)))
            if ed.get("aviso_ia"):   # personas hechas con IA: aviso fijo todo el video
                p = tmpd / "ia.png"; capa(ch, '<div class="ia">Video creado con IA</div>', p, color)
                capas.append((p, 0, 999))
            if ed.get("cierre"):
                c = ed["cierre"]; p = tmpd / "cierre.png"
                img_logo = "" if c.get("sin_logo") else '<img src="' + (base / logo).resolve().as_uri() + '">'
                lado_c = {"derecha": "der", "izquierda": "izq"}.get(c.get("alinear", ""), "")
                capa(ch, f'<div class="z {c.get("zona","abajo")} cierre {lado_c}"><div class="card">{img_logo}<span>{html.escape(c["texto"])}</span></div></div>', p, color)
                capas.append((p, c["t0"], 999))
            ext = ed.get("extender", 0)   # segundos de cuadro congelado al final, para el cierre
            cmd = [ff, "-y", "-v", "error"]
            if r0: cmd += ["-ss", str(r0)]
            if r1: cmd += ["-to", str(r1)]
            cmd += ["-i", str(src)]
            anx = ed.get("anexar")   # {"video": "videos/originales/2D.mp4", "desde": 5, "hasta": 8}: pega un segundo clip al final
            if anx:
                if not (base / anx["video"]).exists():
                    fallas.append(f'{ad["id"]}: no encontré {anx["video"]} para anexar'); continue
                cmd += ["-ss", str(anx.get("desde", 0))] + (["-to", str(anx["hasta"])] if anx.get("hasta") else []) + ["-i", str(base / anx["video"])]
            k0 = 2 if anx else 1
            for p, _, _ in capas: cmd += ["-i", str(p)]
            esc = f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},setsar=1,fps=30"
            if anx:
                f = (f"[0:v]{esc}[a0];[1:v]{esc}[a1];[0:a]aresample=44100[s0];[1:a]aresample=44100[s1];"
                     f"[a0][s0][a1][s1]concat=n=2:v=1:a=1[vc][ac0];[ac0]" + (f"apad=pad_dur={ext}" if ext else "anull") + "[ac];[vc]" + (f"tpad=stop_mode=clone:stop_duration={ext}" if ext else "null") + "[v0]")
            else:
                f = f"[0:v]{esc}" + (f",tpad=stop_mode=clone:stop_duration={ext}" if ext else "") + "[v0]"
            for i, (_, a, b) in enumerate(capas, 1):
                a2, b2 = max(a - (r0 or 0), 0), b - (r0 or 0)
                f += f";[v{i-1}][{i - 1 + k0}:v]overlay=0:0:enable='between(t,{a2:.2f},{b2:.2f})'[v{i}]"
            cmd += ["-filter_complex", f, "-map", f"[v{len(capas)}]", "-map", "[ac]" if anx else "0:a?"] + (["-af", f"apad=pad_dur={ext}"] if ext and not anx else []) + ["-c:v", "libx264", "-preset", "medium", "-crf", "21",
                    "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart", str(dst)]
            r = subprocess.run(cmd, capture_output=True, text=True)
            if r.returncode != 0:
                fallas.append(f'{ad["id"]}: ffmpeg falló: ' + r.stderr.strip()[-300:]); continue
            shutil.rmtree(tmpd, ignore_errors=True)
            print("Video", ad["id"], "→", dst)
    if fallas:
        print("\nHay que corregir esto:", *fallas, sep="\n  "); sys.exit(1)

def transcribir(video):
    try:
        from faster_whisper import WhisperModel
    except ImportError:
        print("No está faster-whisper. Instálalo con: python3 -m pip install --user faster-whisper (en Windows: py -m pip install --user faster-whisper). La primera vez baja un modelo de unos 460 MB. O usa --pausas."); return
    segs, _ = WhisperModel("small", device="cpu", compute_type="int8").transcribe(video, language="es", word_timestamps=True)
    for s in segs:
        print(f"{s.start:.2f}-{s.end:.2f} {s.text.strip()}")
        print("   " + " ".join(f"{w.word.strip()}@{w.start:.2f}" for w in s.words))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    if sys.argv[1] in ("--pausas", "--transcribir") and len(sys.argv) < 3:
        sys.exit(__doc__)
    if sys.argv[1] == "--pausas": pausas(sys.argv[2])
    elif sys.argv[1] == "--transcribir": transcribir(sys.argv[2])
    else: editar(sys.argv[1])
