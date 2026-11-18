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
- **Nunca inventes** reseñas, número de clientes, "más vendido", resultados, ni cuentas regresivas falsas. Si todavía no hay reseñas reales, ese bloque se arma con lo que sí es verdad.
- **Lo que muestras es lo que tiene que llegar.** Las fotos llevan la marca, así que antes de publicar confirma con la persona que el proveedor despacha con su etiqueta (en CJ se pide en la pestaña Customize del producto). Si todavía no, que lo pida antes de prender anuncios.
- Recuérdale revisar la regla sanitaria de su país antes de vender un suplemento o un cosmético.
- En productos de salud, nada de "cura", "elimina" o "trata". Se habla de apoyo y se recomienda consultar al médico.
- Guarda cada aprobación en `contexto/04-tienda.md` con la fecha.

---

## Paso 1 · La estructura (aprobación 1)
Arma el esquema de la página, bloque por bloque, adaptado a su producto. Esta es la estructura base, probada en suplementos y productos de bienestar que venden en Estados Unidos:

**Arriba (lo que se ve sin bajar):**
1. **Barra de anuncio:** la oferta real y "Envío gratis a [país]".
2. **Cinta de beneficios** que se mueve: 5 o 6 beneficios cortos ("60 cápsulas", "Ingredientes naturales", "Envío gratis"…).
3. **Galería de 6 a 8 fotos** a la izquierda (abajo en celular).
4. **El bloque de compra:**
   - Prueba social real, si existe (calificación, unidades vendidas). Si no existe, no va.
   - Una línea de categoría ("Apoyo diario para…").
   - **El título promete el resultado, no nombra el producto.** Ejemplo de forma: "Un estómago tranquilo empieza aquí", no "Cápsulas de orégano 60 unidades".
   - Una frase que explica cómo lo logra.
   - **6 íconos** con beneficios o diferenciales.
   - El precio con el precio de antes tachado solo si la oferta es real.
   - **La oferta por cantidad, en 3 tarjetas:** 1 unidad, la del medio marcada "Más popular" con un regalo o un mejor precio por unidad, y la más grande con envío gratis o 2 regalos. Muestra el precio por unidad en cada una.
   - Los regalos que se desbloquean, si la oferta los tiene.
   - El botón de compra, y debajo la fecha estimada de entrega real según el proveedor, y la garantía en una línea.
   - Desplegables: Descripción, Por qué lo necesitas, Beneficios, Modo de uso, Garantía.

**Abajo (lo que convence):**
5. **Los ingredientes clave** (o los componentes): 3 o 4 tarjetas, cada uno con qué hace en palabras simples.
6. **Prueba:** reseñas reales si existen. Si no, "Lo que vive la gente con [el problema]" con frases del brief presentadas como el problema, no como reseñas del producto.
7. **Los beneficios en grande:** 4 bloques con imagen y texto.
8. **5 razones por las que es distinto** a todo lo que ya probó.
9. **Comparación:** tu marca contra "otras opciones" (sin nombrar ninguna), en una tabla con 4 o 5 filas.
10. **La garantía:** 30 días, explicada en 2 líneas.
11. **La oferta otra vez**, con el botón.
12. **Preguntas frecuentes:** 6 a 8, que respondan las objeciones del brief.

Muéstrale el esquema con lo que va en cada bloque (sin el texto final todavía) y explícale en una línea por qué cada uno está ahí. Ajusta lo que pida y **espera su aprobación**. Guarda el esquema aprobado en `contexto/04-tienda.md`.

## Paso 2 · El copy (aprobación 2)
Escribe todos los textos siguiendo **la skill `copy`** al pie de la letra: la marca hablándole a su cliente en sus palabras, en español fluido, pulido antes de mostrarlo. Bloque por bloque, en el orden del esquema.

Muéstraselo completo y **espera su aprobación**. Guárdalo en `contexto/04-tienda.md`, sección "Copy aprobado".

## Paso 3 · Las fotos y el prototipo visual (aprobación 3)
1. **Las fotos con Higgsfield**, usando los mockups de `marca/` como referencia para que el producto se vea igual en todas:
   1. Foto principal: el producto en fondo limpio con la oferta.
   2. El producto con sus beneficios alrededor (tipo infografía).
   3. Los ingredientes o componentes.
   4. Cómo se usa.
   5. Una persona del cliente ideal usándolo en su día a día.
   6. El antes y después **de la situación** (no de un cuerpo ni de un resultado médico).
   7. La comparación contra otras opciones.
   8. La garantía.
   Y las imágenes de los bloques de abajo (ingredientes y beneficios). Revisa que el nombre en la etiqueta se lea bien en todas; si una sale con letras raras, vuelve a generarla. Guárdalas en `tienda/fotos/`.
2. **El prototipo:** un solo archivo `tienda/prototipo.html` con toda la página, con la paleta, las tipografías, el logo, las fotos y el copy aprobados. Pensado primero para celular (ahí llega casi todo el tráfico de los anuncios), y que se vea bien en computador. Que las tarjetas de oferta se puedan seleccionar y el precio cambie.
3. Ábrelo en su navegador (`open tienda/prototipo.html` en Mac, `start tienda/prototipo.html` en Windows) y pídele que lo mire también en el celular con la vista de celular del navegador.
4. Ajusta lo que pida y **espera su aprobación**.

## Paso 4 · La página en Shopify (aprobación 4)
1. **El producto:** créalo con `shopify store execute --allow-mutations` (mutación `productCreate`) con el título, la descripción, las fotos de `tienda/fotos/` y **una variante por cada tarjeta de la oferta** ("1 frasco", "3 frascos"…) con su precio. Para subir las fotos, usa una mutación de carga de archivos o de medios de producto; si una falla, dile cuál y sigue con las demás.
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
