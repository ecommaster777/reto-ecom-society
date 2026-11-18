---
name: marca
description: Crea la marca del producto del Reto de 4 días de eCom Society antes de montar la tienda: concepto, nombre con dominio disponible, paleta, tipografía, logo, etiqueta (si es un consumible) y mockup del producto con Higgsfield. Úsala cuando la persona escriba "marca", "reto-marca", "nombre", "logo", "colores", "etiqueta", "label" o "mockup", o después de la skill shopify.
---

# Marca del reto

Le creas a una persona principiante la marca de su producto, **antes** de montar la página. La meta es una marca que se vea **brutal**, con personalidad propia, que alguien quiera mostrar y recomendar. No una marca genérica de plantilla.

## Reglas
- Lee `CLAUDE.md` y todo `contexto/`, sobre todo `01-investigacion-mercado.md` (el dolor, a quién le duele, cómo habla) y `02-producto-y-numeros.md` (el producto elegido). Si no hay producto elegido, dile que corra primero la parte 2 de la skill `producto`.
- **La persona aprueba cada paso, uno por uno:** el concepto, el nombre, los colores y la tipografía, el logo, la etiqueta (primero el texto y después el diseño) y el mockup. En cada paso muéstrale las opciones, recomiéndale una, explica por qué en 2 líneas y **espera su respuesta antes de seguir**. Si pide cambios, rehaz solo eso.
- Mientras generas imágenes, avísale en una línea en qué vas ("Haciendo los 3 logos…"), para que sepa que va avanzando aunque esté en clase escuchando. Guarda también las opciones que no eligió.
- **Al final le muestras todo junto** (`marca/marca.html`) como resumen de lo que aprobó.
- **Nunca copies ni nombres otras marcas.** Puedes usar lo que aprendiste de la competencia para diferenciarte, pero ningún nombre, logo, color característico ni frase de otra marca.
- Todo lo que se apruebe va a `contexto/04-tienda.md`, en la sección "Marca", con la fecha. Las imágenes van a la carpeta `marca/` dentro de `mi-reto`.
- Las imágenes se hacen con **Higgsfield**, que quedó conectado el miércoles. Si no aparece (prueba con `/mcp`), dile que corra la skill `herramientas` y vuelva.

## Paso 1 · El concepto
Antes del nombre, la idea. Propón **3 conceptos de marca**, cada uno con:
- La idea en una frase (qué representa la marca para su cliente).
- La personalidad, en 3 palabras.
- Cómo le habla al cliente, con una frase de ejemplo escrita como la marca.
- Por qué se diferencia de lo que ya hay en el mercado.

Que no sean variaciones del mismo concepto. Uno puede ser cálido y cercano, otro técnico y de laboratorio, otro audaz y moderno. Recomienda uno según el cliente del brief.

## Paso 2 · El nombre
1. Propón **8 nombres** para el concepto aprobado. Que sean:
   - Cortos (2 a 3 sílabas idealmente), fáciles de decir y de escribir en español, y que suenen bien en inglés.
   - Propios, no descriptivos: nada de "UricCare", "GotaFree" o "NaturalPlus". Pueden evocar el resultado, un ingrediente o una sensación.
   - Sin palabras médicas ni promesas ("cura", "detox").
2. **Revisa el dominio de cada uno.** Para el .com corre
   `curl -s -o /dev/null -w "%{http_code}" https://rdap.verisign.com/com/v1/domain/NOMBRE.com`
   Si responde 404, está libre; si responde 200, está tomado. Para otros dominios (.co, .mx) usa `whois NOMBRE.co` y busca si dice que no existe. Si el .com está tomado, prueba variaciones naturales (getnombre.com, nombrehealth.com, nombre + país).
3. Revisa también en la web que no haya otra marca grande con ese nombre en la misma categoría.
4. Muéstrale una tabla: nombre, por qué funciona, dominio libre o tomado. Recomienda 2.
5. Cuando lo elija, dile que puede comprar el dominio dentro de Shopify (Configuración › Dominios › Comprar dominio). La compra la hace la persona.

## Paso 3 · La paleta y la tipografía
- **5 colores con su código:** un principal, uno de acento, uno oscuro para textos, uno claro para fondos y uno de apoyo. Explica qué transmite cada uno.
- **Evita el cliché de la categoría** si todos los competidores usan lo mismo (por ejemplo, todo verde en suplementos naturales). Diferenciarse en el estante también es diferenciarse en el feed.
- Revisa que el texto oscuro sobre el fondo claro se lea bien, y también el texto claro sobre el color principal y sobre el de acento (contraste de al menos 4,5 a 1 para textos chicos). Si no da, dilo y usa ese color solo para títulos grandes o fondos con texto oscuro.
- **2 tipografías de Google Fonts:** una para títulos con carácter y una para textos fácil de leer.
- Muéstrale la paleta como una lámina simple en HTML (`marca/paleta.html`), ábrela en su navegador y **espera su aprobación**.

## Paso 4 · El logo
- Genera con Higgsfield **3 propuestas de logo**: el nombre escrito con la tipografía y el estilo del concepto (logotipo), y si suma, un símbolo simple. Fondo plano, sin mockups, sin texto extra.
- Que se lea en tamaño chico (el ícono de una pestaña, la tapa de un frasco).
- Muéstrale las 3, recomiéndale la que mejor se lea en chico y encaje con el concepto, y **espera que elija**. Quítale el fondo a la elegida con la herramienta de quitar fondo de Higgsfield (la página lo usa transparente) y guárdala en `marca/logo.png` y las otras en `marca/logo-opcion-2.png` y `marca/logo-opcion-3.png`.

## Paso 5 · La etiqueta (si es un consumible)
Si el producto se consume (suplemento, crema, bebida, snack, cosmético), la etiqueta va **antes** de todo lo demás, porque es lo que se ve en cada foto.
0. **Primero la foto del proveedor** (ver Paso 6: tómala tú del link de CJ y guárdala en `marca/referencia-proveedor.jpg`). Mírala y anota el color de fondo de su etiqueta: **la etiqueta de la marca usa ese mismo color de fondo**, porque así llega el producto. El logo y los textos van con los colores de la marca. Díselo a la persona en una línea antes de mostrarle el diseño.
1. Escribe primero el contenido de la etiqueta:
   - Nombre de la marca y nombre del producto.
   - El beneficio en pocas palabras, sin promesas de salud ("Apoyo para…", no "Cura…").
   - Ingredientes clave y presentación (por ejemplo "60 cápsulas · 1 mes").
   - En suplementos: "Suplemento alimenticio" y el modo de uso. Avísale que el texto legal final depende de su país y de su fabricante.
   Muéstrale el texto y **espera su aprobación** antes de diseñar.
2. Genera con Higgsfield **2 diseños de etiqueta** planos, de frente, con el color de fondo de la etiqueta del proveedor, el logo y los colores de la marca para los textos.
   Antes de mostrarlos, **lee letra por letra el texto de cada imagen** contra el texto aprobado, tildes incluidas (por ejemplo "Úrico", no "Urico"). Si uno tiene un error, vuelve a generarlo; no le muestres a la persona una etiqueta con errores.
3. Muéstrale los 2, recomiéndale el que mejor se lea y **espera que elija**. Guarda el elegido en `marca/etiqueta.png` (el otro en `marca/etiqueta-opcion-2.png`).
4. Recuérdale, al final, que antes de vender un suplemento con su marca revise el registro sanitario de su país (INVIMA en Colombia, COFEPRIS en México) y que la etiqueta cumpla la norma (FDA en Estados Unidos).

## Paso 6 · El mockup del producto
- **El mockup se parece al producto real del proveedor, con su marca.** Si ya la tomaste en el Paso 5, úsala. Si no, toma tú la foto principal del producto desde su link de CJ (está en `contexto/02-producto-y-numeros.md`): ábrelo con Claude en Chrome o descárgala de la página y guárdala en `marca/referencia-proveedor.jpg`. Solo si no puedes bajarla, pídele a la persona que la descargue y la arrastre a la terminal. Úsala como primera referencia en Higgsfield: misma forma de envase, mismo tamaño, mismo tipo de tapa y de etiqueta. Lo único que cambia es la marca: la etiqueta y el logo aprobados (`marca/etiqueta.png` y `marca/logo.png` como segunda referencia). Así lo que muestra la página es lo que le llega al cliente cuando el proveedor ponga su etiqueta.
- **Los colores del empaque son los del proveedor.** Si el frasco del proveedor es amarillo, el mockup es amarillo, aunque la paleta de la marca sea otra: el logo y los textos van con los colores de la marca, pero el envase, la tapa y el color de fondo de la etiqueta se quedan como llegan. Si el cliente ve un frasco rojo y le llega uno amarillo, pide reembolso. Las cápsulas también se ven del color real.
- Pide una foto de producto realista: luz natural, sombra suave, fondo liso cálido, sin aspecto de render 3D.
- Para productos que no son consumibles, el mockup es el producto con el logo y su empaque.
- **3 tomas:** fondo limpio de estudio (la foto principal), el producto en un ambiente que encaje con el concepto, y el producto con sus ingredientes o en uso.
- Revisa que el nombre se lea bien, sin errores de ortografía, y que la etiqueta sea la misma en todas. Si una sale con otra etiqueta o con letras raras, vuelve a generarla usando la primera toma aprobada como referencia.
- Guarda las mejores en `marca/mockup-1.png`, `marca/mockup-2.png` y `marca/mockup-3.png`. Son la base de las fotos de la página. Muéstraselas y **espera su aprobación**.

## Al terminar
Escribe en `contexto/04-tienda.md` la sección "Marca": concepto, personalidad, cómo habla la marca, nombre, dominio, colores con códigos, tipografías y la ruta de cada imagen. Arma `marca/marca.html` con todo junto (concepto, nombre, paleta, logo con sus opciones, etiqueta y los 3 mockups), ábrelo en su navegador como resumen de todo lo que aprobó.

Dile el siguiente paso: correr la skill `tienda`.
