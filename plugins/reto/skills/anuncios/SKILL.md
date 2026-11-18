---
name: anuncios
description: Hace los anuncios del Reto de 4 días de eCom Society y deja la campaña lista para montar a mano en Meta. Elige los 3 ángulos con más urgencia y más mercado, arma 3 conjuntos con 5 anuncios cada uno en formatos distintos (imagen nativa, imagen UGC, imagen de beneficios, comparación u oferta, video animado y video UGC con IA o de producto), con sus textos, los videos editados en la zona segura de Reels y la guía de la campaña. Úsala cuando la persona escriba "anuncios", "reto-anuncios", "creativos", "campaña" o "ads", o en la clase del viernes.
---

# Anuncios del reto

Acompañas a una persona **principiante** a sacar sus anuncios y dejar su campaña prendida para revisarla el domingo. Ella aprueba; tú haces los anuncios, los textos y la guía. La campaña la monta ella a mano en el Administrador de anuncios.

## Reglas
- Lee `CLAUDE.md` y todo `contexto/`: la investigación (`01`), el producto y sus números (`02`), la marca y la tienda (`04`) y el perfil con su ruta y su presupuesto (`00-perfil.md`). Si no hay página de producto, dile que primero corra la skill `tienda`.
- Una pregunta a la vez. La persona responde solo 2 veces: **los 3 ángulos junto con el "sí" a los créditos** (Paso 1) y **los anuncios terminados** (Paso 4). Entre una y otra vas solo, avisando en una línea qué estás haciendo.
- `RUTA` es la carpeta donde está este archivo SKILL.md (ahí está `plantilla/`).
- **Antes de empezar, revisa que esté ffmpeg** (`ffmpeg -version`). Si falta: Mac `brew install ffmpeg` (si no hay `brew`, primero instala Homebrew desde https://brew.sh); Windows `winget install Gyan.FFmpeg`, y después cerrar Claude Code y la terminal y abrirlos de nuevo (si no, no lo encuentra).
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
- **Siempre "suplemento".** Si el anuncio habla de medicamentos, agrega "no reemplaza un tratamiento médico" (sin "tu médico"). Nunca sugieras dejar un tratamiento.
- Sin promesas de tiempo ("en 7 días").

## Paso 1 · Los 3 ángulos (aprobación 1)
1. Saca de `contexto/01-investigacion-mercado.md` los dolores, los deseos y las frases textuales de la gente.
2. Califica cada uno de 1 a 5 en **urgencia** (qué tan fuerte, frecuente y de "lo necesito ya" es) y en **tamaño de mercado** (a cuánta gente le pasa: cuántas frases lo repiten y lo que dice la investigación).
3. Muéstrale una tabla ordenada por urgencia × tamaño y recomiéndale los **3 primeros**, distintos entre sí: un dolor fuerte, una alternativa u objeción y un deseo funcionan bien juntos.
4. Para cada ángulo: nombre corto, el ángulo en una frase y por qué (con cuántas frases lo repiten).
5. **En el mismo mensaje**, dile cuántos créditos de Higgsfield vas a gastar en total (unos 160, incluidas las fotos nuevas) y su saldo, y pídele las dos cosas juntas: "¿Apruebas estos 3 ángulos y que gaste unos 160 créditos?". Espera su "sí". Así no te quedas parado esperando mientras ella está en clase.

## Paso 2 · Los 15 anuncios (vas solo)
Cada ángulo es un **conjunto de anuncios** con 5 formatos distintos. **Regla de oro de los creativos: ninguna imagen se parece a otra.** Si dos anuncios comparten plantilla, foto, paleta o encuadre, para Meta son el mismo anuncio. Las 9 imágenes usan 9 combinaciones distintas de plantilla, foto y estilo de texto, y como máximo una selfie en toda la campaña. Los videos animados también van cada uno en un estilo distinto (por ejemplo 3D, papel recortado, acuarela) y nunca comparten metraje. Para las fotos nuevas (unboxing, flat lay, macro de un ingrediente, fondo de noche) usa `gpt_image_2_6` en 4:5 con la foto del producto como referencia y guárdalas en `anuncios/fuentes/`.

| Letra | Formato | Cómo se hace | Créditos |
|---|---|---|---|
| A | Imagen nativa (parece una publicación normal) | Una plantilla distinta en cada conjunto: `postit` (nota escrita a mano sobre una foto), `post` (publicación), `calendario` (la semana en el celular) o `nota` (app de notas). Evita `bloqueo` (pantalla bloqueada con notificaciones): Meta puede verlo como una función falsa del teléfono | 0 |
| B | Imagen UGC | Plantilla `ugc` con una foto distinta en cada conjunto: unboxing (manos abriendo la caja), flat lay (desayuno desde arriba), selfie con el producto. Textos `estilo`: normal (cajas blancas), `marcador` (letra a mano resaltada) o `pie` | 0 a 0,25 por foto nueva |
| C | Imagen de marca | Una distinta en cada conjunto: `editorial` (foto a sangre y titular de revista), `beneficios`, `comparacion` u `oferta` | 0 a 0,25 |
| D | Video animado | Imagen 9:16 en estilo de película animada 3D, después Kling 8 s | unos 16 |
| E | Conjunto 1: video UGC con IA (15 s). Conjuntos 2 y 3: video de producto (8 s) | Marketing Studio / Kling | 75 / 16 |

**Total: unos 160 créditos** (más 1 de las imágenes de inicio y lo que haya que repetir). Si no le alcanzan, cambia el video UGC con IA por uno de producto (16).

### 2.1 · El archivo de la campaña
Copia `plantilla/campana-ejemplo.json` a `anuncios/campana.json` y reemplaza **todo**:
- **Marca:** los datos de `tienda/pagina/datos.json`, con las rutas relativas a `anuncios/` (antepón `../tienda/pagina/`). Si no hay `logo_claro`, haz una versión blanca del logo con `ffmpeg -i tienda/pagina/fotos/logo.png -vf "lutrgb=r=255:g=255:b=255" tienda/pagina/fotos/logo-claro.png` (conserva el fondo transparente).
- **Países e idioma:** ruta A, todos los países que quedaron en `contexto/02` y el idioma de su página; ruta B, solo su país.
- **Presupuesto y moneda:** de `00-perfil.md` (si no está, el equivalente a USD 30 al día). `moneda`, `presupuesto_diario` y `cpa_max` van siempre en la moneda de **su cuenta publicitaria** (la de su tarjeta), convertidos si hace falta.
- **`cpa_max`:** lo que puede pagar por venta, de `contexto/02`. Si hay varios países, usa el número más bajo.
- **URL:** la de su página de producto.
- **Conjuntos y anuncios:** usa sus fotos de la página, nunca fotos del proveedor.

### 2.2 · Los textos de cada anuncio (con la skill `copy`)
- **Texto principal:** 3 párrafos cortos. El gancho (una escena vivida, nunca un titular), qué es el producto y por qué ayuda, y la oferta.
- **Título:** máximo 40 caracteres. **Descripción:** máximo 30.
- Ningún texto se repite entre los 15. Rota los cierres: envío gratis, garantía, el paquete.
- **Ruta A (varios países): no pongas precios en dólares** en las imágenes, los videos ni los textos, porque Meta se los muestra a gente que paga en otra moneda. Habla de la oferta ("lleva 3 y paga 2", "el 2.º a mitad de precio") y de la garantía.

### 2.3 · Los videos en Higgsfield (los créditos ya los aprobó en el Paso 1)
1. Sube a Higgsfield la foto principal del producto (`media_upload`, sube el archivo al link que te da y `media_confirm`).
2. **La imagen de inicio de cada video tiene que ser vertical (9:16).** Guárdalas en `anuncios/fuentes/`. Si la foto de la página no lo es, primero haz una 9:16 con `gpt_image_2_6` usando la foto como referencia. Con una imagen cuadrada el video sale cuadrado y al pasarlo a vertical se cortan cabezas y frascos.
3. **D, video animado:** imagen con `gpt_image_2_6`, `aspect_ratio: "9:16"`, la foto del producto como referencia y "3D animated film style, Pixar-like", la escena del ángulo y "the exact bottle from the reference, same label and colors". Después `kling3_0` con `duration: 8`, `aspect_ratio: "9:16"`, esa imagen como `start_image` y el movimiento.
4. **E, video UGC con IA (conjunto 1):** `marketing_studio_video` con `aspect_ratio: "9:16"`, `resolution: "720p"` (en 1080p cuesta más del doble), la foto del producto en `medias` con rol `image`, y en el prompt la persona (edad y estilo de su cliente), el lugar y **el guion exacto** de 30 a 45 palabras en su español, cumpliendo las reglas de Meta.
5. **E, video de producto (conjuntos 2 y 3):** `kling3_0`, `duration: 8`, `aspect_ratio: "9:16"`, desde una imagen 9:16 (alguien tomando la cápsula, o el frasco en estudio con un movimiento lento de cámara).
6. Espera con `jobs_wait` y baja cada video con `curl -L --create-dirs "<url>" -o anuncios/videos/originales/<ID>.mp4` (en Windows, `curl.exe` en vez de `curl`). Míralos y escúchalos: si el frasco sale deformado o con otras letras, o el audio trae una voz rara, repite ese (en Kling, repite con `sound: "off"`).

### 2.4 · La edición de los videos
Cada video lleva títulos o subtítulos, siempre en la **zona segura de Reels** (Instagram tapa el 14 % de arriba y el 35 % de abajo) y **nunca encima de una cara**.
1. Mira un cuadro de cada video (`ffmpeg -ss 2 -i video.mp4 -frames:v 1 cuadro.jpg`) y fíjate dónde está la cara y dónde el frasco.
2. En `campana.json`, a cada anuncio de video ponle `original` (el de `videos/originales/`), `video` (`videos/<ID>.mp4`) y `edicion`:
   - **Videos sin voz:** 2 títulos cortos (del segundo 0 al 3 y del 3 al 5,5); el primero es el gancho del ángulo, no una lista de ingredientes. Van en la zona sin cara (`arriba`, `centro` o `abajo`). Después un `cierre` con la oferta: mira el cuadro de ese segundo; si el producto está en el centro, usa `"zona": "arriba"` y `"sin_logo": true` para no tapar la etiqueta, o recorta el video antes de que el producto llene el cuadro.
   - **Video con voz:** subtítulos con lo que dice la persona. Como el guion lo escribiste tú, usa `python3 RUTA/plantilla/editar_video.py --pausas video.mp4` para ver en qué segundos habla y reparte el guion en esos tramos (solo si el audio no coincide, usa `--transcribir`, que necesita faster-whisper y baja unos 460 MB la primera vez), en frases de 3 a 8 palabras, `estilo: "subtitulo"`, en la zona sin cara. Si el producto está a un lado, alinea los subtítulos al otro con `"alinear": "derecha"` o `"izquierda"`. Agrega `"extender": 2` y un `cierre` con la oferta.
   - **Todo video donde aparezca una persona realista hecha con IA** (hable o no) lleva `"aviso_ia": true`, que pone "Video creado con IA".
3. Corre `python3 "RUTA/plantilla/editar_video.py" anuncios/campana.json` (con comillas: en Windows la ruta puede tener espacios). Necesita ffmpeg: si falta, instálalo (Mac: `brew install ffmpeg`; Windows: `winget install Gyan.FFmpeg`, y cerrar y volver a abrir Claude Code y la terminal).
4. Revisa un cuadro de cada video editado: textos completos, dentro de la zona segura y sin tapar caras ni la etiqueta.

### 2.5 · Arma todo
```
python3 "RUTA/plantilla/armar_anuncios.py" anuncios/campana.json
```
Hace las imágenes de 1080 × 1350 en `anuncios/imagenes/`, la página `anuncios/revision.html` y la guía `anuncios/campana.md` (y `campana.html` para leerla cómoda). Si dice que falta algo, corrígelo y vuelve a correrlo. Mira cada imagen: ningún texto cortado ni encima del producto.

## Paso 3 · Revisa tú antes de mostrar
Lee los 15 textos, las 9 imágenes y los 6 videos contra las reglas de Meta de arriba (busca "tu" o "tus" junto a una condición, síntoma o tratamiento, "crisis", "cura", "previene", "no reemplaza a tu médico" (mejor: "no reemplaza un tratamiento médico"), likes inventados) y corrige. Revisa que la URL sea la de su página y que lo que dicen los anuncios (precio, envío gratis, regalos, garantía) sea exactamente lo que dice su página: si la página da envío gratis desde 2 frascos, ningún anuncio promete envío gratis en 1 frasco.

## Paso 4 · Los anuncios terminados (aprobación 2)
Abre `anuncios/revision.html` en su navegador (así se ven en el celular, con sus textos) y pídele que los revise. Cambia lo que pida y vuelve a correr el paso 2.5.

## Paso 5 · Montar la campaña (la persona, un paso a la vez)
Antes, revisa con ella dos cosas, porque sin ellas no se prende:
- **Su tienda cobra:** pasarela aprobada y página publicada. Si no, la campaña queda armada en borrador y la publica el día que la aprueben.
- **Su página no tiene nada de muestra ni frases prohibidas.** Meta revisa la página igual que los anuncios. Quita (o cambia por lo real): las reseñas y los videos de testimonio de muestra, "Compra verificada", el número de clientes ("Más de 1.200 clientes") y frases como "Gente real, resultados reales". Pasa la página por las mismas reglas de salud: nada de "tu ácido úrico" o "tu [condición]", nada de "que no vuelva". Si hay que cambiarla, hazlo con la skill `tienda` antes de publicar la campaña.

Abre `anuncios/campana.html` en su navegador y las carpetas `anuncios/imagenes` y `anuncios/videos` (Finder o Explorador). Avísale que **nunca suba los de `videos/originales/`**: esos no tienen títulos ni cierre. Guíala **un paso a la vez**, esperando su "¿Listo?" en cada uno:
1. https://adsmanager.facebook.com › **+ Crear** › objetivo **Ventas** › **Campaña de ventas Advantage+**. Presupuesto **de la campaña** (Advantage+) por el monto diario.
2. **Conjunto 1:** su píxel y el evento **Compra**; los países y el idioma; público Advantage+ sin intereses (edad mínima 25 en los controles; la edad de su cliente va como sugerencia); ubicaciones Advantage+.
3. **Anuncio:** su página de Facebook y su cuenta de Instagram; sube el archivo; pega texto principal, título y descripción; botón **Comprar**; la URL de su página (la misma en todos) y, en "Parámetros de URL", lo que dice la guía. **Apaga una por una las mejoras de Advantage+ creative** (mejoras de texto, superposiciones, expandir imagen, generar fondo, música, animación, traducción, comentarios relevantes, anuncios de varios anunciantes): pueden cambiar el texto o la imagen y romper las reglas de salud.
4. Los otros 4 anuncios del conjunto: duplica el anuncio y cambia archivo, textos y nombre.
5. **Conjuntos 2 y 3:** duplica el conjunto 1 ya armado, cámbiale el nombre y en cada anuncio cambia archivo, textos y nombre. Si Meta no deja duplicar dentro de la campaña Advantage+, que la cree otra vez con la configuración manual.
6. **Publicar.** Meta los revisa en minutos o en unas horas.

Si Meta le frena la cuenta o el pago, que lleve la captura al grupo: la tarea cuenta igual con la campaña armada. Si el evento **Compra** sale restringido (Meta a veces limita las tiendas de salud, sobre todo en Estados Unidos), que saque Estados Unidos del conjunto o lleve la captura al grupo.

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
