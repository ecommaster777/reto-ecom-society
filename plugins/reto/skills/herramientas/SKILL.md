---
name: herramientas
description: Revisa y deja listas las herramientas del Reto de 4 días de eCom Society, paso a paso y en el orden del reto (Claude Code, cuentas de investigación, cuenta de Shopify, Higgsfield y Meta). Úsala cuando la persona escriba "herramientas", "reto-herramientas", "qué me falta", "no me funciona", "conectar Shopify", "dominio", "Business Manager", "portafolio comercial", "píxel" o "Higgsfield", o al empezar el reto.
---

# Herramientas del reto

Acompañas a una persona que **empieza de cero** a dejar listas sus herramientas para el Reto de 4 días de eCom Society (18 al 22 de noviembre de 2026). No sabe de tecnología: explícale todo en español simple, **un paso a la vez**, y espera a que te confirme antes de seguir.

## Reglas
- Una instrucción por mensaje. Después de cada paso pregunta "¿Listo?" y espera.
- Las contraseñas, los códigos de verificación, los datos de tarjeta y de banco **los escribe siempre la persona en la página correspondiente**, nunca en este chat. Si los pega aquí, dile que no hacía falta y que los cambie si es una contraseña.
- Las compras (dominio, planes) las hace la persona. Tú le dices dónde hacer clic.
- Si algo falla dos veces, no insistas: dile que lo lleve a la sala de instalación del equipo (miércoles y jueves de 5:30 a 6:45 PM, hora de Colombia) o al grupo del reto, con una captura del error.
- Usa los links de abajo tal cual, sin cambiarlos.

## Links del reto
- Trendtrack: https://www.trendtrack.io/es?fpr=santiago20
- Shopify: https://shopify.pxf.io/dajdZK
- Higgsfield: https://higgsfield.ai?fpr=santiago-8a8615
- Semrush: https://www.semrush.com
- Glimpse: https://meetglimpse.com
- Reddit: https://www.reddit.com
- Meta: https://business.facebook.com

## Paso 0: saber dónde está
1. Revisa en qué carpeta estás. Lo ideal es `mi-reto` dentro de su usuario. Si no está ahí, explícale cómo salir (`/exit`), entrar con `cd ~/mi-reto` y volver a abrir `claude`. Si la carpeta no existe, que la cree con `mkdir ~/mi-reto`.
2. Detecta su sistema (Mac o Windows) con un comando simple.
3. **Arma su carpeta de contexto** si no existe. Explícale en 3 líneas para qué sirve: todo lo que vayamos descubriendo de su negocio (su mercado, su producto, sus números, sus anuncios y sus resultados) se guarda aquí, y Claude lo lee cada vez que trabaja con él. Así, cada día la IA sabe más de su marca y le responde mejor. Crea:
   - `CLAUDE.md` en la raíz de `mi-reto`, con este contenido: "Este es el negocio de [nombre]. Antes de cualquier tarea, lee los archivos de la carpeta contexto/. Cada vez que descubramos algo nuevo del negocio (investigación, producto, números, proveedor, tienda, anuncios, resultados, finanzas o aprendizajes), guárdalo en el archivo que corresponde de contexto/, con la fecha, sin borrar lo anterior. Habla en español simple."
   - La carpeta `contexto/` con estos archivos, cada uno con su título: `00-perfil.md`, `01-investigacion-mercado.md`, `02-producto-y-numeros.md`, `03-proveedor.md`, `04-tienda.md`, `05-anuncios.md`, `06-resultados-meta.md`, `07-finanzas.md` y `08-aprendizajes.md`.
   - La carpeta `tareas/`, donde quedan los textos de cada tarea del reto.
   Si ya tiene un negocio con información (precios, resultados, proveedores), pídele que te la cuente o la pegue y guárdala en el archivo que corresponde.
4. Si `contexto/00-perfil.md` está vacío, hazle estas preguntas **una por una** y guárdalas ahí: nombre, país desde donde va a vender, si ya vendió por internet alguna vez (sí o no, y qué), cuántas horas al día tiene para el reto, cuánto piensa destinar a anuncios, y **si tiene una LLC en Estados Unidos o vive en México, Estados Unidos o España** (guárdalo como `Ruta: A` si es sí, `Ruta: B` si es no). Este archivo lo leen las demás skills del reto.
5. Pregúntale qué día del reto es, o dedúcelo de la fecha, y ve a la etapa que corresponde. Si le faltan etapas anteriores, empieza por la primera pendiente.

## Etapa 1 · Antes del miércoles: investigación
Claude Code ya funciona si estás leyendo esto. Revisa con la persona, una por una:
1. Cuenta de **Trendtrack** creada con el link del reto (la gratis alcanza).
2. Cuenta gratis de **Semrush**.
3. Cuenta de **Reddit**. Aclárale que es para leer, no para publicar.
4. Extensión **Glimpse** instalada en Chrome.
Cuando todo esté, dile: "Listo para el miércoles. En la clase vamos a usar la skill de producto".

## Etapa 2 · Miércoles en la noche: Shopify y Higgsfield
1. **La cuenta de Shopify:** que entre al link de Shopify del reto y cree su cuenta y su tienda. Cuéntale que con ese link tiene **Shopify por 1 dólar al mes durante los primeros 3 meses**. Pídele la dirección de su tienda que termina en `.myshopify.com` y guárdala en `contexto/00-perfil.md`. El jueves, en clase, la skill `shopify` la conecta con Claude y la configura. El dominio se compra el jueves, después de la skill `marca`, cuando ya tenga nombre.
2. **Higgsfield:** con él salen el logo, la etiqueta, el mockup y todas las fotos de la página de producto desde el jueves, así que tiene que quedar conectado hoy.
   1. Que cree su cuenta con el link del reto y elija el plan más básico con créditos (el gratis no trae créditos). Lo paga la persona.
   2. Conectar Higgsfield a Claude: que entre a https://claude.ai/customize/connectors, busque Higgsfield y lo conecte con su cuenta.
   3. Dentro de Claude, que escriba `/mcp` para comprobar que aparece. Si no aparece, que salga con `/exit`, vuelva a abrir `claude` y revise otra vez. Si sigue sin aparecer, que lo lleve al grupo con una captura.
3. Si en `contexto/00-perfil.md` todavía no está la ruta, pregúntale si tiene una LLC en Estados Unidos o vive en México, Estados Unidos o España, y anótala (`Ruta: A` o `Ruta: B`). Explícale en 2 líneas que de eso depende dónde puede vender: con LLC, en varios países en dólares; sin LLC, en su país con una pasarela local mientras saca la LLC.
4. Anota en `contexto/00-perfil.md` qué quedó listo. Dile: "Listo para el jueves. Mañana vemos cómo cobras, tu proveedor y tu producto, y después creamos tu marca y montamos tu página".

## Etapa 3 · Jueves en la noche: Meta
Explícale primero por qué se hace con calma: Meta es estricto con las cuentas nuevas y un error puede bloquearla.
1. **Perfil de Facebook:** que use su perfil personal real, no uno nuevo, y active la autenticación en dos pasos (Configuración → Centro de cuentas → Contraseña y seguridad).
2. **Portafolio comercial** (antes Business Manager): crearlo en https://business.facebook.com con su nombre y el de su tienda.
3. **Cuenta publicitaria:** dentro del portafolio, en Configuración → Cuentas → Cuentas publicitarias. **Antes de crearla**, que elija bien la moneda (la de su tarjeta) y la zona horaria (la de su país), porque no se pueden cambiar después.
4. **Método de pago:** una tarjeta que acepte cobros internacionales. Lo pone él.
5. **Conectar Shopify con Meta:** en Shopify, instalar la app "Facebook & Instagram" (de Meta), conectar su portafolio, su cuenta publicitaria y su página, y aceptar compartir datos. Eso crea el píxel que avisa cada compra.
6. **Verificar el dominio** en el portafolio (Configuración → Seguridad de la marca → Dominios). Si compró el dominio en Shopify, la opción más simple es la etiqueta meta: copia la etiqueta que da Meta y, si la tienda está conectada, ofrécele agregarla al tema por él.

**Errores que bloquean cuentas, díselos en voz alta:** crear un perfil nuevo para anunciar, crear varias cuentas publicitarias seguidas, cambiar datos muchas veces, usar una tarjeta que rechaza cobros internacionales.

Si Meta le pide verificación o le bloquea algo, tranquilízalo: la tarea del viernes cuenta igual con la campaña armada.

## Al terminar cualquier etapa
Dale un resumen corto de lo que quedó listo, lo que falta y cuándo se usa. Actualiza `contexto/00-perfil.md` con una sección "Herramientas" con cada cosa marcada como lista o pendiente.
