---
name: tienda
description: Monta la página de producto del Reto de 4 días de eCom Society en 4 pasos con aprobación (estructura, copy, prototipo visual en HTML con fotos de Higgsfield, y la página publicada en Shopify), con una estructura probada para suplementos y productos de salud y bienestar. Úsala cuando la persona escriba "tienda", "reto-tienda", "página de producto", "montar mi tienda", "prototipo" o "subir a Shopify", o después de la skill marca.
---

# Tienda del reto

Le montas a una persona principiante **la página de producto** de su marca, la que va a recibir el tráfico de los anuncios. Se hace en 4 pasos y **la persona aprueba cada uno antes de seguir**:

1. La estructura.
2. El copy.
3. El prototipo visual en HTML.
4. La página en Shopify.

## Reglas
- Lee `CLAUDE.md` y todo `contexto/`. Necesitas: el brief (`01`), el producto con sus números y su oferta (`02`), el proveedor y el tiempo de entrega (`03`) y la marca y el setup de Shopify (`04`). Si falta la marca, corre primero la skill `marca`; si la tienda no está conectada, la skill `shopify`.
- **Nunca uses fotos del proveedor.** Todas las imágenes salen de Higgsfield a partir de los mockups de `marca/`.
- **Nunca nombres otras marcas**, ni en la página ni al explicarle a la persona. Usa lo que aprendiste de ellas sin mencionarlas.
- **Precios en dólares.** La tienda se configura en USD y Shopify Markets convierte a la moneda de cada país al que vende. Solo si la persona vende en un único país, los precios van en su moneda local.
- **Reseñas de muestra:** en el prototipo y en la primera versión de Shopify van reseñas, fotos de clientes y número de clientes de muestra, hechos con IA, para que la página esté completa. Anótalo en `contexto/04-tienda.md` y recuérdale que **antes de prender anuncios** se reemplazan por reseñas reales. Las cuentas regresivas van a una fecha real.
- **Lo que muestras es lo que tiene que llegar.** Las fotos llevan la marca, así que antes de publicar confirma con la persona que el proveedor despacha con su etiqueta (en CJ se pide en la pestaña Customize del producto). Si todavía no, que lo pida antes de prender anuncios.
- Recuérdale revisar la regla sanitaria de su país antes de vender un suplemento o un cosmético.
- En productos de salud, nada de "cura", "elimina" o "trata". Se habla de apoyo y se recomienda consultar al médico.
- Guarda cada aprobación en `contexto/04-tienda.md` con la fecha.

---

## Paso 1 · La estructura (aprobación 1)
Arma el esquema de la página con **esta arquitectura, en este orden** (29 bloques). Está tomada de una de las páginas de suplementos que más vende en Estados Unidos; adapta los textos y las fotos a su producto, pero respeta los bloques y sus elementos.

**Arriba (lo que se ve sin bajar):**
1. **Barra de oferta** con el nombre de la oferta y una cuenta regresiva a una fecha real (por ejemplo, el fin de la oferta de lanzamiento).
2. **Encabezado:** menú, logo al centro, buscador y carrito.
3. **Cinta de beneficios** que se mueve, con 5 o 6 beneficios cortos.
4. **Galería deslizable:** foto principal con un sello ("Regalos gratis"), flechas a los lados y puntos debajo en celular, miniaturas en computador. Se desliza con el dedo, sin barra de scroll.
5. **Prueba social:** estrellas, "Más de X clientes" y 4 o 5 caritas de clientes.
6. **Categoría** en una línea ("Apoyo diario para…") y **título con el resultado**, en una sola línea.
7. **Una frase** que explica cómo lo logra.
8. **6 beneficios con ícono**, en 2 columnas.
9. **Precio:** el del paquete elegido, el precio de antes tachado y una etiqueta con el ahorro.
10. **3 tarjetas de paquete:** "Compra 1" · "Compra 1 y el 2.º va al 50 %" (marcada "Más popular", con envío gratis) · "Compra 2 y llévate 1 gratis" (marcada "Mejor precio", con envío gratis y un regalo). Cada una con su foto, precio por unidad y precio tachado. Antes de proponerlas, calcula el margen de cada oferta con el costo real del proveedor para esa cantidad y su envío: las 3 tienen que dejar **al menos 60 %** después del producto, el envío y la pasarela. Si una no da, súbele el precio base o cambia esa oferta.
11. **Regalos desbloqueados:** 3 casillas (envío gratis, regalo 1, regalo 2) que se activan según el paquete.
12. **Fecha de entrega:** "Pide hoy y te llega entre el [fecha] y el [fecha]", calculada con el tiempo real del proveedor.
13. **Botón** "Agregar al carrito" con el precio tachado y el precio final dentro.
14. **Suscripción** en una línea: "Se renueva cada 30 días · Cancela cuando quieras".
15. **Desplegables:** Descripción, ¿Por qué [marca]?, Tus regalos, Beneficios, Cómo tomarlo, ¿Tienen garantía?

**Abajo (lo que convence):**
16. **Bloque oscuro** con una idea fuerte, un número grande y el botón "Pruébalo sin riesgo".
17. **Ingredientes en carrusel:** una tarjeta por ingrediente con foto real de cerca y qué hace por la persona.
18. **Reseñas:** tira de fotos de clientes con el producto y carrusel de reseñas con estrellas, título, texto, nombre, ciudad y "Compra verificada".
19. **Bloque oscuro "Siéntete mejor cada día":** 3 íconos de beneficio y la foto del producto.
20. **Beneficios reales:** 4 filas, cada una con foto de estilo de vida, título del resultado, una línea y un "+".
21. **Botón**, y otra vez la cinta de beneficios.
22. **5 razones** en carrusel: foto, etiqueta "Razón 1…5", título y una línea.
23. **Comparación** contra "otras marcas" (sin nombrar ninguna): tu producto contra un envase genérico, con 2 o 3 diferencias.
24. **Garantía de 30 días** con sello, texto, botón y la foto de una persona sonriendo con el producto.
25. **Gente real, resultados reales:** 3 videos o fotos verticales de clientes hablando a la cámara con el producto.
26. **La oferta otra vez:** "Compártelo con tu familia", las 3 tarjetas, la fecha y el botón.
27. **Preguntas frecuentes** que resuelven las objeciones del brief (cuándo noto la diferencia, si lo puedo tomar con medicamento, qué lleva, efectos, envío, pago seguro, garantía, cancelar la suscripción), con un botón al final.
28. **Lista de reseñas** con etiquetas ("Uso diario", "Recompra"…).
29. **Pie de página:** correo para ofertas, links (preguntas, contacto, rastreo, envíos, devoluciones, privacidad, términos), las advertencias de salud y el selector de país y moneda.

**Reglas de conversión (CRO):**
- Menos scroll y menos fricción: poco espacio entre secciones (unos 32 px en celular), títulos de una sola línea, párrafos de 1 o 2 líneas.
- Un **botón fijo abajo en celular** que aparece cuando la persona pasa el botón principal.
- Todo carrusel se desliza con el dedo, tiene flechas o puntos que indican que se puede deslizar y nunca muestra barra de scroll.
- WhatsApp flotante.

Muéstrale el esquema adaptado a su producto, bloque por bloque, sin el texto final todavía. Ajusta lo que pida y **espera su aprobación**. Guarda el esquema aprobado en `contexto/04-tienda.md`.

## Paso 2 · El copy (aprobación 2)
Escribe todos los textos siguiendo **la skill `copy`** al pie de la letra: la marca hablándole a su cliente en sus palabras, en español fluido, pulido antes de mostrarlo. Bloque por bloque, en el orden del esquema.

Muéstraselo completo y **espera su aprobación**. Guárdalo en `contexto/04-tienda.md`, sección "Copy aprobado".

## Paso 3 · Las fotos y el prototipo visual (aprobación 3)
1. **Las fotos con Higgsfield**, usando el mockup aprobado de `marca/` como referencia en todas para que el producto se vea igual. **Tienen que parecer fotos reales tomadas con un celular, no imágenes de IA ni gráficos:** luz natural, casas y lugares comunes del país del cliente, personas de la edad del cliente con piel real y sin retoque, encuadres imperfectos. Agrega al prompt: "candid iPhone photo, natural light, real skin texture, unretouched, everyday home, not a studio shot". Nada de textos ni infografías dentro de las fotos: los textos van en la página.
   1. Galería (6): el producto en fondo liso, el producto con el regalo, una persona del cliente ideal sosteniéndolo en su casa, la mano con las cápsulas o el producto en uso, el producto en su lugar de todos los días (buró, cocina), el ingrediente principal de cerca.
   2. Ingredientes: una foto real de cerca de cada uno.
   3. Clientes (4 o 5): fotos tipo selfie de personas distintas sosteniendo el producto, para la tira de reseñas.
   4. Beneficios (4): escenas del resultado que quiere la persona (caminar, jugar con los nietos, comer con la familia, tomarlo en la mañana).
   5. Garantía: retrato de una persona sonriendo con el producto.
   6. Videos de clientes (3): **videos de verdad que se reproducen**, no fotos con un ícono de play. Primero la foto vertical tipo selfie y después, con Higgsfield (imagen a video con sonido, unos 8 segundos), la persona diciendo una frase corta en el español de su país. Comprímelos para web (unos 540 px de ancho) antes de ponerlos en la página.
   8. **El producto sin fondo:** quítale el fondo al mockup con Higgsfield y usa ese recorte cada vez que el producto va sobre un fondo de color o dentro de una pieza del carrusel, para que flote con su sombra y no se vea como una foto pegada en un recuadro.
   7. Comparación: un envase genérico sin marca. Revisa que el nombre en la etiqueta se lea bien en todas; si una sale con letras raras, vuelve a generarla. Guárdalas en `tienda/fotos/`.
   Las 7 piezas del carrusel (producto con 3 beneficios, siéntete mejor, por qué confiar, testimonio, cápsulas con 6 detalles, comparación e información nutrimental) se arman en HTML con las fotos y se exportan a imagen **al doble de resolución** (2160 px), para que el texto y las fotos se vean nítidos en celular. Si una foto se va a ver grande, escálala antes a 2K.
2. **El prototipo:** un solo archivo `tienda/prototipo.html` con toda la página, con la paleta, las tipografías, el logo, las fotos y el copy aprobados. Pensado primero para celular (ahí llega casi todo el tráfico de los anuncios), y que se vea bien en computador. Que las tarjetas de oferta se puedan seleccionar y el precio cambie.
3. Ábrelo en su navegador (`open tienda/prototipo.html` en Mac, `start tienda/prototipo.html` en Windows) y pídele que lo mire también en el celular con la vista de celular del navegador.
4. Ajusta lo que pida y **espera su aprobación**.

## Paso 4 · La página en Shopify (aprobación 4)
1. **El producto:** créalo con `shopify store execute --allow-mutations` y la mutación `productCreate`, con el título, la descripción y la opción "Paquete" con un valor por cada tarjeta de la oferta ("1 frasco", "2 frascos", "3 frascos"), con precios en dólares. Después fija el precio de cada variante con `productVariantsBulkUpdate`. Sube las fotos de `tienda/fotos/` con `stagedUploadsCreate` y después `productCreateMedia`; si una falla, dile cuál y sigue con las demás.
2. **La plantilla:** baja su tema con `shopify theme pull --store SU-TIENDA.myshopify.com --live --path tienda/tema`. Crea:
   - `sections/pagina-reto.liquid`, con el prototipo convertido a Liquid. El bloque de compra usa el formulario de producto de Shopify, con las variantes como tarjetas de oferta y el botón de agregar al carrito funcionando. Los colores, fuentes y textos salen del prototipo aprobado.
   - `templates/product.reto.json`, que usa esa sección.
3. **Súbelo como tema sin publicar:** `shopify theme push --store SU-TIENDA.myshopify.com --unpublished --theme "Pagina Reto" --path tienda/tema --json`. Si pide iniciar sesión, la persona lo hace en el navegador. El resultado trae el link de vista previa y el id del tema: anótalos en `contexto/04-tienda.md`.
4. Asígnale al producto la plantilla `reto` (campo `templateSuffix` con `productUpdate`, también con `--allow-mutations`).
5. Dale el link de vista previa del tema y pídele que la revise en el celular: fotos, textos, que las tarjetas cambien el precio y que el botón agregue al carrito. Ajusta lo que pida y **espera su aprobación**.
6. Cuando apruebe y te diga "publícalo", publica el tema con `shopify theme publish --store SU-TIENDA.myshopify.com --theme ID-DEL-TEMA`. Agrega el producto al menú principal y crea la página "Sobre nosotros" con la historia de la marca en el tono aprobado.

## Al terminar
Actualiza `contexto/04-tienda.md` con el link de la tienda, el link del producto y lo que quedó pendiente (dominio, pasarela, reseñas). Escribe el texto de la tarea 2 en `tareas/tarea-2.txt`:

```
TAREA 2 · [Nombre] · [País]
Mi marca: [nombre] · [dominio]
Mi página: [link del producto]
Mis 3 números: me cuesta [X] puesto en la casa · lo vendo en [Y] · puedo pagar [Z] por venta
Mi pasarela: [cuál, conectada o pendiente]
```

Recuérdale publicarlo en el grupo de WhatsApp antes del viernes a las 5 PM, hora de Colombia, y correr esta noche la skill `herramientas` para dejar listo Meta.
