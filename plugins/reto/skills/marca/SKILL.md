---
name: marca
description: Crea la marca del producto del Reto de 4 días de eCom Society antes de montar la tienda: concepto, nombre con dominio disponible, paleta, tipografía, logo, etiqueta (si es un consumible) y mockup del producto con Higgsfield. Úsala cuando la persona escriba "marca", "reto-marca", "nombre", "logo", "colores", "etiqueta", "label" o "mockup", o después de la skill shopify.
---

# Marca del reto

Le creas a una persona principiante la marca de su producto, **antes** de montar la página. La meta es una marca que se vea **brutal**, con personalidad propia, que alguien quiera mostrar y recomendar. No una marca genérica de plantilla.

## Reglas
- Lee `CLAUDE.md` y todo `contexto/`, sobre todo `01-investigacion-mercado.md` (el dolor, a quién le duele, cómo habla) y `02-producto-y-numeros.md` (el producto elegido). Si no hay producto elegido, dile que corra primero la parte 2 de la skill `producto`.
- **Un paso a la vez, y la persona aprueba cada uno** antes de seguir. Muéstrale opciones, recomiéndale una y explica por qué en 2 líneas.
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
- Revisa que el texto oscuro sobre el fondo claro se lea bien.
- **2 tipografías de Google Fonts:** una para títulos con carácter y una para textos fácil de leer.
- Muéstrale la paleta como una lámina simple en HTML (`marca/paleta.html`) y ábrela en su navegador.

## Paso 4 · El logo
- Genera con Higgsfield **3 propuestas de logo**: el nombre escrito con la tipografía y el estilo del concepto (logotipo), y si suma, un símbolo simple. Fondo plano, sin mockups, sin texto extra.
- Que se lea en tamaño chico (el ícono de una pestaña, la tapa de un frasco).
- La persona elige una; ajústala si pide cambios. Guarda la elegida en `marca/logo.png`.

## Paso 5 · La etiqueta (si es un consumible)
Si el producto se consume (suplemento, crema, bebida, snack, cosmético), la etiqueta va **antes** de todo lo demás, porque es lo que se ve en cada foto.
1. Escribe primero el contenido de la etiqueta y muéstraselo:
   - Nombre de la marca y nombre del producto.
   - El beneficio en pocas palabras, sin promesas de salud ("Apoyo para…", no "Cura…").
   - Ingredientes clave y presentación (por ejemplo "60 cápsulas · 1 mes").
   - En suplementos: "Suplemento alimenticio" y el modo de uso. Avísale que el texto legal final depende de su país y de su fabricante.
2. Cuando lo apruebe, genera con Higgsfield **2 diseños de etiqueta** planos, de frente, con la paleta y el logo. La persona elige.
3. Guarda la elegida en `marca/etiqueta.png`.

## Paso 6 · El mockup del producto
- **El mockup se parece al producto real del proveedor, con su marca.** Pídele a la persona la foto del producto en CJ (o del proveedor) y úsala como primera referencia en Higgsfield: misma forma de envase, mismo tamaño, mismo tipo de tapa y de etiqueta. Lo único que cambia es la marca: la etiqueta y el logo aprobados (`marca/etiqueta.png` y `marca/logo.png` como segunda referencia). Así lo que muestra la página es lo que le llega al cliente cuando el proveedor ponga su etiqueta.
- Pide una foto de producto realista: luz natural, sombra suave, fondo liso cálido, sin aspecto de render 3D.
- Para productos que no son consumibles, el mockup es el producto con el logo y su empaque.
- **3 tomas:** fondo limpio de estudio (la foto principal), el producto en un ambiente que encaje con el concepto, y el producto con sus ingredientes o en uso.
- Revisa que el nombre se lea bien y que la etiqueta sea la misma en todas. Si una sale con letras raras, vuelve a generarla.
- Guarda las aprobadas en `marca/mockup-1.png`, `marca/mockup-2.png` y `marca/mockup-3.png`. Son la base de las fotos de la página.

## Al terminar
Escribe en `contexto/04-tienda.md` la sección "Marca": concepto, personalidad, cómo habla la marca, nombre, dominio, colores con códigos, tipografías y la ruta de cada imagen. Muéstrale un resumen con todo junto (puedes armarlo en `marca/marca.html` y abrirlo en su navegador).

Dile el siguiente paso: correr la skill `tienda`.
