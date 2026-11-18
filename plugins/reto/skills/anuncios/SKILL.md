---
name: anuncios
description: Hace los anuncios del Reto de 4 días de eCom Society y deja la campaña lista para montar a mano en Meta. Elige los 3 ángulos con más urgencia y más mercado, arma 3 conjuntos con 5 anuncios cada uno en formatos distintos (imagen nativa, imagen UGC, imagen de beneficios, comparación u oferta, video animado y video UGC con IA o de producto), con sus textos, los videos editados en la zona segura de Reels y la guía de la campaña. Úsala cuando la persona escriba "anuncios", "reto-anuncios", "creativos", "campaña" o "ads", o en la clase del viernes.
---

# Anuncios del reto

Acompañas a una persona **principiante** a sacar sus anuncios y dejar su campaña prendida para revisarla el domingo. Ella aprueba; tú haces los anuncios, los textos y la guía. La campaña la monta ella a mano en el Administrador de anuncios.

## Reglas
- Lee `CLAUDE.md` y todo `contexto/`: la investigación (`01`), el producto y sus números (`02`), la marca y la tienda (`04`) y el perfil con su ruta y su presupuesto (`00-perfil.md`). Si no hay página de producto, dile que primero corra la skill `tienda`.
- Una pregunta a la vez. Solo 2 aprobaciones: **los 3 ángulos** (Paso 1) y **los anuncios terminados** (Paso 4). Entre las dos vas solo, avisando en una línea qué estás haciendo.
- **Antes de gastar créditos de Higgsfield, dile cuántos vas a gastar y espera su "sí".** Revisa su saldo con la herramienta de balance de Higgsfield.
- Todo va en la carpeta `anuncios/`. Lo aprobado se anota en `contexto/05-anuncios.md`, con la fecha, sin borrar lo anterior.
- **Nunca nombres otras marcas** en los anuncios.
- En Windows, donde dice `python3` escribe `py`.
- Si algo falla dos veces, no insistas: que lo lleve al grupo del reto con una captura.

## Las reglas de Meta para salud y suplementos (no se negocian)
Si un anuncio rompe una, Meta lo rechaza o frena la cuenta. Revisa cada texto, cada imagen y cada video:
- **Nunca le digas a la persona lo que tiene.** Nada de "¿Tienes gota?", "tu ácido úrico", "tu gota", "tus crisis", "si sufres de…". Di "el ácido úrico", habla de la escena en tercera persona ("quien lo vivió lo sabe…") o del ingrediente.
- **Nada de curar, eliminar, tratar ni prevenir.** Tampoco "antes de que duela", "que no vuelva", "la próxima crisis". Usa "apoyo", "cuidar", "para tu rutina", "niveles saludables".
- **Nada de antes y después**, ni partes del cuerpo con defectos marcados.
- **Ningún testimonio inventado.** Las personas de las fotos y los videos hechos con IA nunca dicen "a mí me funcionó" ni dan resultados: explican o recomiendan. Las imágenes UGC llevan la nota "Imagen creada con IA" (la plantilla la pone sola).
- **Nada falso:** ni likes o comentarios inventados, ni afirmaciones sobre la competencia que no puedas probar.
- **Siempre "suplemento".** Si el anuncio habla de medicamentos, agrega que no reemplaza lo que indicó el médico. Nunca sugieras dejar un tratamiento.
- Sin promesas de tiempo ("en 7 días").

## Paso 1 · Los 3 ángulos (aprobación 1)
1. Saca de `contexto/01-investigacion-mercado.md` los dolores, los deseos y las frases textuales de la gente.
2. Califica cada uno de 1 a 5 en **urgencia** (qué tan fuerte, frecuente y de "lo necesito ya" es) y en **tamaño de mercado** (a cuánta gente le pasa: cuántas frases lo repiten y lo que dice la investigación).
3. Muéstrale una tabla ordenada por urgencia × tamaño y recomiéndale los **3 primeros**, distintos entre sí: un dolor fuerte, una alternativa u objeción y un deseo funcionan bien juntos.
4. Para cada ángulo: nombre corto, el ángulo en una frase y por qué (con cuántas frases lo repiten). Espera su aprobación.

## Paso 2 · Los 15 anuncios (vas solo)
Cada ángulo es un **conjunto de anuncios** con 5 formatos distintos:

| Letra | Formato | Cómo se hace | Créditos |
|---|---|---|---|
| A | Imagen nativa | Plantilla `nota` (app de notas) o `post` (publicación), con una foto de su página | 0 |
| B | Imagen UGC | Plantilla `ugc`: foto de su página con una persona y el producto, 2 burbujas de texto | 0 |
| C | Imagen de marca | Una distinta en cada conjunto: `beneficios`, `comparacion` u `oferta` (3 frascos y el precio) | 0 |
| D | Video animado | Imagen 9:16 en estilo de película animada 3D, después Kling 8 s | unos 16 |
| E | Conjunto 1: video UGC con IA (15 s). Conjuntos 2 y 3: video de producto (8 s) | Marketing Studio / Kling | 75 / 16 |

**Total: unos 160 créditos**, más lo que haya que repetir. Si no le alcanzan, cambia el video UGC con IA por uno de producto (16).

### 2.1 · El archivo de la campaña
Copia `plantilla/campana-ejemplo.json` a `anuncios/campana.json` y reemplaza **todo**:
- **Marca:** los datos de `tienda/pagina/datos.json`, con las rutas relativas a `anuncios/` (antepón `../tienda/pagina/`). Si no hay `logo_claro`, haz una versión blanca del logo (mismo dibujo, color blanco, fondo transparente) y guárdala en `tienda/pagina/fotos/logo-claro.png`.
- **Países e idioma:** ruta A, todos los países que quedaron en `contexto/02` y el idioma de su página; ruta B, solo su país.
- **Presupuesto y moneda:** de `00-perfil.md` (si no está, USD 30 al día); en la ruta B, en la moneda de su cuenta publicitaria.
- **`cpa_max`:** lo que puede pagar por venta, de `contexto/02`. Si hay varios países, usa el número más bajo.
- **URL:** la de su página de producto.
- **Conjuntos y anuncios:** usa sus fotos de la página, nunca fotos del proveedor.

### 2.2 · Los textos de cada anuncio (con la skill `copy`)
- **Texto principal:** 3 párrafos cortos. El gancho (una escena vivida, nunca un titular), qué es el producto y por qué ayuda, y la oferta.
- **Título:** máximo 40 caracteres. **Descripción:** máximo 30.
- Ningún texto se repite entre los 15. Rota los cierres: envío gratis, garantía, precio por día, el paquete.

### 2.3 · Los videos en Higgsfield (antes, los créditos y su "sí")
1. Sube a Higgsfield la foto principal del producto (`media_upload`, sube el archivo al link que te da y `media_confirm`).
2. **La imagen de inicio de cada video tiene que ser vertical (9:16).** Si la foto de la página no lo es, primero haz una 9:16 con `gpt_image_2_6` usando la foto como referencia. Con una imagen cuadrada el video sale cuadrado y al pasarlo a vertical se cortan cabezas y frascos.
3. **D, video animado:** imagen con `gpt_image_2_6`, `aspect_ratio: "9:16"`, la foto del producto como referencia y "3D animated film style, Pixar-like", la escena del ángulo y "the exact bottle from the reference, same label and colors". Después `kling3_0` con `duration: 8`, `aspect_ratio: "9:16"`, esa imagen como `start_image` y el movimiento.
4. **E, video UGC con IA (conjunto 1):** `marketing_studio_video` con `aspect_ratio: "9:16"`, `resolution: "720p"` (en 1080p cuesta más del doble), la foto del producto en `medias` con rol `image`, y en el prompt la persona (edad y estilo de su cliente), el lugar y **el guion exacto** de 30 a 45 palabras en su español, cumpliendo las reglas de Meta.
5. **E, video de producto (conjuntos 2 y 3):** `kling3_0`, `duration: 8`, `aspect_ratio: "9:16"`, desde una imagen 9:16 (alguien tomando la cápsula, o el frasco en estudio con un movimiento lento de cámara).
6. Espera con `jobs_wait` y baja cada video con `curl -L "<url>" -o anuncios/videos/originales/<ID>.mp4`. Míralos: si el frasco sale deformado o con otras letras, repite ese.

### 2.4 · La edición de los videos
Cada video lleva títulos o subtítulos, siempre en la **zona segura de Reels** (Instagram tapa el 14 % de arriba y el 35 % de abajo) y **nunca encima de una cara**.
1. Mira un cuadro de cada video (`ffmpeg -ss 2 -i video.mp4 -frames:v 1 cuadro.jpg`) y fíjate dónde está la cara y dónde el frasco.
2. En `campana.json`, a cada anuncio de video ponle `original` (el de `videos/originales/`), `video` (`videos/<ID>.mp4`) y `edicion`:
   - **Videos sin voz:** 2 títulos cortos (del segundo 0 al 3 y del 3 al 5,5), en la zona sin cara (`arriba` o `abajo`), y un `cierre` con la oferta, donde no tape la etiqueta.
   - **Video con voz:** subtítulos con lo que dice la persona. Sácalo con `python3 RUTA/plantilla/editar_video.py --transcribir video.mp4` (si no está faster-whisper, con `--pausas` y el guion), en frases de 3 a 8 palabras, `estilo: "subtitulo"`, en la zona sin cara. Agrega `"extender": 2` y un `cierre` con el precio para que termine con la oferta.
3. Corre `python3 RUTA/plantilla/editar_video.py anuncios/campana.json`. Necesita ffmpeg: si falta, instálalo (Mac: `brew install ffmpeg`; Windows: `winget install Gyan.FFmpeg` y volver a abrir la terminal).
4. Revisa un cuadro de cada video editado: textos completos, dentro de la zona segura y sin tapar caras ni la etiqueta.

### 2.5 · Arma todo
```
python3 RUTA/plantilla/armar_anuncios.py anuncios/campana.json
```
Hace las imágenes de 1080 × 1350 en `anuncios/imagenes/`, la página `anuncios/revision.html` y la guía `anuncios/campana.md` (y `campana.html` para leerla cómoda). Si dice que falta algo, corrígelo y vuelve a correrlo. Mira cada imagen: ningún texto cortado ni encima del producto.

## Paso 3 · Revisa tú antes de mostrar
Lee los 15 textos, las 9 imágenes y los 6 videos contra las reglas de Meta de arriba (busca "tu ", "crisis", "cura", "previene", likes inventados) y corrige. Revisa que todas las URL sean la de su página.

## Paso 4 · Los anuncios terminados (aprobación 2)
Abre `anuncios/revision.html` en su navegador (así se ven en el celular, con sus textos) y pídele que los revise. Cambia lo que pida y vuelve a correr el paso 2.5.

## Paso 5 · Montar la campaña (la persona, un paso a la vez)
Antes, revisa con ella dos cosas, porque sin ellas no se prende:
- **Su tienda cobra:** pasarela aprobada y página publicada. Si no, la campaña queda armada en borrador y la publica el día que la aprueben.
- **Su página no tiene nada de muestra:** en `contexto/04` las reseñas de muestra hechas con IA ya están cambiadas por reseñas reales (o quitadas). Meta revisa la página.

Abre `anuncios/campana.html` en su navegador y la carpeta `anuncios/imagenes` (Finder o Explorador). Guíala **un paso a la vez**, esperando su "¿Listo?" en cada uno:
1. https://adsmanager.facebook.com › **+ Crear** › objetivo **Ventas**. Presupuesto **de la campaña** (Advantage+) por el monto diario.
2. **Conjunto 1:** su píxel y el evento **Compra**; los países y el idioma; público Advantage+ sin intereses (edad mínima 25 en los controles; la edad de su cliente va como sugerencia); ubicaciones Advantage+.
3. **Anuncio:** su página de Facebook y su cuenta de Instagram; sube el archivo; pega texto principal, título y descripción; botón **Comprar**; la URL. **Apaga las "mejoras de Advantage+ creative"** (pueden reescribir el texto o generar variaciones y romper las reglas de salud).
4. Los otros 4 anuncios del conjunto: duplica el anuncio y cambia archivo, textos y URL.
5. **Conjuntos 2 y 3:** duplica el conjunto 1 ya armado, cámbiale el nombre y en cada anuncio cambia archivo, textos y URL.
6. **Publicar.** Meta los revisa en minutos o en unas horas.

Si Meta le frena la cuenta o el pago, que lleve la captura al grupo: la tarea cuenta igual con la campaña armada.

## Paso 6 · Hasta el domingo
Dile claro: **no se toca nada hasta la clase del domingo.** Ni presupuesto, ni anuncios, ni públicos. El domingo se revisa todo con el protocolo de optimización. Su número para el domingo es lo que puede pagar por venta (`cpa_max`).

## Al terminar
Anota en `contexto/05-anuncios.md`: los 3 ángulos con su porqué, los 15 anuncios (ID, formato, archivo y textos), presupuesto, países y la fecha en que la prendió.

Escribe `tareas/tarea-3.txt`, listo para pegar en el grupo de WhatsApp:
```
TAREA 3 · [Nombre] · [País]
Mi marca: [nombre] · [dominio]
Mis 3 ángulos: [ángulo 1] · [ángulo 2] · [ángulo 3]
Mis anuncios: 3 conjuntos × 5 anuncios ([formatos])
Presupuesto: [moneda] [x] al día · Países: [lista]
Estado: prendida el [fecha] / armada (la prendo cuando [motivo])
[Adjunta 3 de tus anuncios y una captura de tu campaña]
```

Dile el siguiente paso: el domingo, en la clase final, revisamos su campaña con el protocolo de optimización.
