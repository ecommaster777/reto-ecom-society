---
name: tienda
description: Monta la página de producto del Reto de 4 días de eCom Society con una plantilla fija, copiada bloque por bloque de una de las páginas de suplementos que más venden en Estados Unidos. La persona aprueba 4 pasos (estructura, copy, prototipo con fotos de Higgsfield y la página publicada en Shopify). Úsala cuando la persona escriba "tienda", "reto-tienda", "página de producto", "montar mi tienda", "prototipo" o "subir a Shopify", o después de la skill marca.
---

# Tienda del reto

Le montas a una persona principiante **la página de producto** de su marca, la que va a recibir el tráfico de los anuncios.

**La página NO se diseña: se llena una plantilla fija.** En la carpeta `plantilla/` junto a esta skill está todo el diseño, la estructura de 29 bloques, el carrusel de 7 piezas y la versión para Shopify. Tú solo llenas un archivo de datos (`datos.json`) con la marca, los colores, las fotos, los textos y las ofertas de la persona. Así todas las páginas del reto quedan iguales en estructura y diseño, y solo cambia el contenido. **Nunca edites `pdp-reto.css`, `pdp-reto.js`, `galeria-reto.css` ni `galeria-reto.js`.**

Archivos de la plantilla:
- `datos-ejemplo.json`: la página completa del producto de ejemplo. Es tu molde: copia su forma campo por campo.
- `armar.py`: junta la plantilla con los datos y deja la página (`index.html`), el carrusel (`galeria.html`) y, si le das la carpeta del tema, la versión para Shopify.
- `exportar_galeria.py`: exporta las 7 piezas del carrusel a imagen al doble de resolución.

Se hace en 4 pasos y **la persona aprueba cada uno antes de seguir**.

## Reglas
- Lee `CLAUDE.md` y todo `contexto/`: el brief (`01`), el producto, los números y la oferta (`02`), el proveedor y el tiempo de entrega (`03`) y la marca y el setup de Shopify (`04`). Si falta la marca, corre primero la skill `marca`; si la tienda no está conectada, la skill `shopify`.
- **Nunca uses fotos del proveedor.** Todas las imágenes salen de Higgsfield a partir del mockup de `marca/`.
- **Lo que muestras es lo que tiene que llegar:** el envase de las fotos tiene la forma y los colores del producto real del proveedor (ver la skill `marca`). Antes de prender anuncios, la persona pide al proveedor su etiqueta (en CJ, pestaña Customize).
- **Nunca nombres otras marcas** en la página. Usa lo que aprendiste de ellas sin mencionarlas.
- **Precios en dólares.** La tienda va en USD y Shopify Markets convierte a cada moneda. En Shopify, los precios de la página salen de las variantes del producto, así que se convierten solos.
- **Reseñas de muestra:** en el prototipo y en la primera versión de Shopify van reseñas, fotos y videos de clientes y número de clientes de muestra, hechos con IA, para que la página esté completa. Anótalo en `contexto/04-tienda.md` y recuérdale que **antes de prender anuncios** se reemplazan por reseñas reales.
- La cuenta regresiva va a una fecha real (el fin de su oferta de lanzamiento).
- Copy: sigue la skill `copy` (resultado antes que características, títulos de una línea, nunca cruces ni asteriscos al final de los textos, nada de "cura", "elimina" o "trata").
- Recuérdale revisar la regla sanitaria de su país antes de vender un suplemento o un cosmético.
- Guarda cada aprobación en `contexto/04-tienda.md` con la fecha. Trabaja en la carpeta `tienda/pagina/` de `mi-reto`.

---

## Paso 1 · La estructura (aprobación 1)
La estructura es fija. Muéstrale los 29 bloques con lo que va a ir en cada uno para **su** producto (sin el texto final todavía), en una lista corta:

**Arriba:** 1 barra de oferta con cuenta regresiva · 2 encabezado con logo · 3 cinta de beneficios · 4 carrusel de 7 piezas · 5 estrellas y caritas de clientes · 6 categoría y título con el resultado · 7 una frase · 8 seis beneficios · 9 precio con ahorro · 10 tres paquetes · 11 regalos desbloqueados · 12 fecha de entrega · 13 botón con el precio · 14 suscripción · 15 desplegables.
**Abajo:** 16 bloque oscuro con un número grande · 17 ingredientes en carrusel · 18 reseñas con fotos de clientes · 19 "siéntete mejor" con el producto sin fondo · 20 beneficios reales con fotos · 21 botón y cinta · 22 cinco razones · 23 comparación contra otras marcas (6 puntos) · 24 garantía · 25 videos de clientes · 26 la oferta otra vez · 27 preguntas frecuentes · 28 lista de reseñas · 29 pie con advertencias y país.

**Los 3 paquetes** (bloque 10): "Compra 1" · "Compra 1 y el 2.º va al 50 %" (Más popular) · "Compra 2 y llévate 1 gratis" (Mejor precio). Antes de proponerlos, calcula con el costo real del proveedor para 1, 2 y 3 unidades con envío y la pasarela: **cada uno tiene que dejar al menos 60 % de margen**. Si uno no da, súbele el precio base o cambia esa oferta, y explícale la cuenta.

Ajusta lo que pida (por ejemplo los regalos o los nombres de las ofertas) y **espera su aprobación**.

## Paso 2 · El copy (aprobación 2)
Copia `plantilla/datos-ejemplo.json` a `tienda/pagina/datos.json` y reemplaza **todos** los textos por los de su marca, siguiendo la skill `copy`. Respeta la forma del archivo: mismos campos, mismas cantidades (6 íconos, 3 ofertas, 3 ingredientes, 3 reseñas con foto, 4 beneficios, 5 razones, 6 filas de comparación, 3 videos, 6 a 8 preguntas frecuentes, 3 reseñas de lista). En el bloque `carrusel` van los textos de las 7 piezas (3 recuadros, 3 íconos, 4 sellos y 6 puntos de confianza, el testimonio, 6 detalles, 5 filas de comparación y la información nutrimental con lo que diga la etiqueta real del proveedor; si no hay dosis, sin dosis).

Íconos disponibles: gota, persona, corazon, check, rayo, escudo, capsula, fruta, hoja, montana, sol, vaso, frasco, mas, chat, estrella, camion.

Muéstrale el copy ordenado por bloque, ajusta y **espera su aprobación**.

## Paso 3 · Las fotos y el prototipo (aprobación 3)
1. **Las fotos con Higgsfield**, con el mockup aprobado de `marca/` como referencia en todas. Tienen que parecer fotos reales de celular: luz natural, casas y lugares comunes del país del cliente, personas de la edad del cliente, piel real sin retoque. Agrega al prompt "candid iPhone photo, natural light, real skin texture, unretouched, everyday home, not a studio shot". Nada de textos dentro de las fotos. Guárdalas en `tienda/pagina/fotos/` **con exactamente los nombres que usa `datos.json`**:
   - `principal.jpg` el producto en fondo liso · `hero-regalo.jpg` el producto con el regalo · `hombre-cocina.jpg` una persona del cliente ideal con el producto en casa · `capsulas-mano.jpg` el producto en uso o en la mano · `buro.jpg` el producto en su lugar de todos los días · `tomando-capsula.jpg` alguien usándolo.
   - `cerezas.jpg` y `semillas.jpg` (o los nombres que pongas en datos) un ingrediente o componente de cerca cada uno.
   - `ugc-1.jpg` a `ugc-4.jpg` selfies de clientes con el producto.
   - `paseo-perro.jpg`, `cena-familia.jpg`, `abuelo-futbol.jpg` escenas del resultado que quiere la persona (cámbiales el nombre en datos si son otras escenas).
   - `garantia-retrato.jpg` una persona sonriendo con el producto.
   - `video-1.jpg` a `video-3.jpg` cuadros verticales tipo selfie, y con ellos **los videos** `video-1.mp4` a `video-3.mp4`: imagen a video con sonido en Higgsfield, unos 8 segundos, la persona diciendo una frase corta en el español de su país. Comprímelos a 540 px de ancho (`ffmpeg -i entrada.mp4 -vf scale=540:-2 -crf 26 -movflags +faststart salida.mp4`).
   - `otra-marca.jpg` un envase genérico sin marca, de aspecto común.
   - `frasco.png` **el producto sin fondo** (quítale el fondo al mockup con Higgsfield y recórtalo): flota sobre los fondos de color.
   - `logo.png` el logo con fondo transparente.
   - Para el carrusel, escala a 2K con Higgsfield las fotos que se ven grandes y guárdalas como `principal-hd.jpg`, `garantia-retrato-hd.jpg` y `capsulas-macro-hd.jpg` (una foto de cerca del producto o de su contenido sobre el color principal).
2. **Arma el prototipo y el carrusel:**
   ```
   python3 RUTA_DE_LA_SKILL/plantilla/armar.py tienda/pagina/datos.json tienda/pagina
   python3 RUTA_DE_LA_SKILL/plantilla/exportar_galeria.py tienda/pagina
   ```
   El segundo comando deja `fotos/galeria-1.png` … `galeria-7.png` a 2160 px. En `datos.json`, la lista `galeria` apunta a esas 7 imágenes (cambia `.jpg` por `.png` o conviértelas a JPG de calidad 88). Vuelve a correr `armar.py`.
3. Ábrelo (`open tienda/pagina/index.html` en Mac, `start tienda\pagina\index.html` en Windows) y pídele que lo revise también en vista de celular. Revisa tú: que ningún título se parta en dos líneas en celular, que el producto de las fotos se vea igual en todas y que el texto de las piezas del carrusel se lea.
4. Ajusta en `datos.json` lo que pida (nunca en los archivos de la plantilla) y **espera su aprobación**.

## Paso 4 · La página en Shopify (aprobación 4)
Usa `shopify store execute --allow-mutations` para todo lo que cambie la tienda.
0. **Moneda, mercados y envío.** Lee la ruta en `contexto/00-perfil.md` y los países en `contexto/02-producto-y-numeros.md`. Lo que no se pueda por la conexión, hazlo con Claude en Chrome en el administrador de la persona.
   - **Ruta B:** la tienda en la moneda de su país y **un solo mercado, su país**. Nada de otros países: su pasarela local no les puede cobrar.
   - **Ruta A:** la moneda de la tienda es USD. Crea los mercados con los países que dejó la skill `producto` en `contexto/02-producto-y-numeros.md` (Estados Unidos, Canadá, Reino Unido, Australia y los de Latinoamérica hispana donde el proveedor envía y el margen da al menos 60 %). **Nunca Argentina.** Shopify Markets convierte el precio a la moneda de cada país. Solo si la persona vende en un único país, la moneda va en la de ese país.
   - **Envío gratis** a su país (ruta B) o a todos esos países (ruta A), con una tarifa de 0 por zona, porque el envío ya va dentro del precio.
1. **El producto:** créalo con `productCreate` con el título y la descripción, y la opción "Paquete" con 3 valores en el mismo orden de las ofertas ("1 frasco", "2 frascos", "3 frascos"). Con `productVariantsBulkUpdate` pon a cada variante su **precio** y su **precio de antes** (`compareAtPrice`) en la moneda de la tienda (dólares en la ruta A, la de su país en la ruta B), iguales a los de las ofertas. Sube `principal.jpg` como foto del producto.
2. **El tema:** bájalo con `shopify theme pull --store SU-TIENDA.myshopify.com --live --path tienda/tema`.
3. **La plantilla:** corre
   ```
   python3 RUTA_DE_LA_SKILL/plantilla/armar.py tienda/pagina/datos.json tienda/pagina tienda/tema
   ```
   Copia al tema la sección, el layout, la plantilla `product.reto`, los estilos y **todas las fotos y videos** a `assets/`. Si dice que faltan imágenes, agrégalas y vuelve a correrlo.
4. **Súbelo sin publicar:** `shopify theme push --store SU-TIENDA.myshopify.com --unpublished --theme "Pagina Reto" --path tienda/tema --json`. Si pide iniciar sesión, la persona lo hace en el navegador. Anota el id del tema y el link de vista previa en `contexto/04-tienda.md`.
5. Asígnale al producto la plantilla `reto` (`productUpdate` con `templateSuffix: "reto"`).
6. Dale el link de vista previa del producto y pídele que revise en el celular: que se vea igual al prototipo, que las tarjetas cambien el precio, que los videos suenen y que el botón lleve al checkout con el paquete elegido. Ajusta y **espera su aprobación**.
7. Cuando diga "publícalo": `shopify theme publish --store SU-TIENDA.myshopify.com --theme ID-DEL-TEMA`. Agrega el producto al menú y crea la página "Sobre nosotros" con la historia de la marca.

## Antes de prender anuncios (la skill `anuncios` lo pide)
Meta revisa la página igual que los anuncios. Las reseñas, los videos de testimonio y el número de clientes del prototipo son **de muestra**: hay que cambiarlos por reales o quitarlos.
1. En `tienda/pagina/datos.json`: si no hay reseñas reales todavía, deja vacías las listas `resenas.items`, `videos.items` y `lista_resenas.items`, borra `prueba.texto` y `resenas.verificada`. La plantilla esconde sola esos bloques cuando están vacíos.
2. Revisa todos los textos con las reglas de salud de la skill `copy`: nada de "tu ácido úrico" (o tu condición), nada de "que no vuelva", nada de testimonios de personas hechas con IA.
3. Vuelve a correr `armar.py` con la carpeta del tema y sube el tema otra vez (Paso 4, puntos 3 y 4).

## Al terminar
Actualiza `contexto/04-tienda.md` con el link de la tienda, el del producto y lo pendiente (dominio, pasarela, etiqueta del proveedor, reseñas reales). Escribe el texto de la tarea 2 en `tareas/tarea-2.txt`:

```
TAREA 2 · [Nombre] · [País]
Mi marca: [nombre] · [dominio]
Mi página: [link del producto]
Mis 3 números: me cuesta [X] puesto en la casa · lo vendo en [Y] · puedo pagar [Z] por venta
Mi pasarela: [cuál, conectada o pendiente]
```

Recuérdale publicarlo en el grupo de WhatsApp antes del viernes a las 5 PM, hora de Colombia, y correr esta noche la skill `herramientas` para dejar listo Meta.
