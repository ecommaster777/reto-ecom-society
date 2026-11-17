---
name: herramientas
description: Revisa y deja listas las herramientas del Reto de 4 días de eCom Society, paso a paso y en el orden del reto (Claude Code, cuentas de investigación, Shopify, dominio, conexión de Shopify con Claude, Meta y Higgsfield). Úsala cuando la persona escriba "herramientas", "reto-herramientas", "qué me falta", "no me funciona", "conectar Shopify", "dominio", "Business Manager", "portafolio comercial", "píxel" o "Higgsfield", o al empezar el reto.
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
3. Si no existe `perfil.md` en la carpeta, hazle estas preguntas **una por una** y guárdalas ahí: nombre, país desde donde va a vender, si ya vendió por internet alguna vez (sí o no, y qué), cuántas horas al día tiene para el reto, y cuánto piensa destinar a anuncios. Este archivo lo leen las demás skills del reto.
4. Pregúntale qué día del reto es, o dedúcelo de la fecha, y ve a la etapa que corresponde. Si le faltan etapas anteriores, empieza por la primera pendiente.

## Etapa 1 · Antes del miércoles: investigación
Claude Code ya funciona si estás leyendo esto. Revisa con la persona, una por una:
1. Cuenta de **Trendtrack** creada con el link del reto (la gratis alcanza).
2. Cuenta gratis de **Semrush**.
3. Cuenta de **Reddit**. Aclárale que es para leer, no para publicar.
4. Extensión **Glimpse** instalada en Chrome.
Cuando todo esté, dile: "Listo para el miércoles. En la clase vamos a usar la skill de producto".

## Etapa 2 · Miércoles en la noche: Shopify, dominio y conexión con Claude
1. **Crear la tienda:** que entre al link de Shopify del reto, cree su cuenta y su tienda. Pídele que te diga la dirección de su tienda que termina en `.myshopify.com` (está en la barra del navegador o en Configuración). Guárdala en `perfil.md`.
2. **El dominio:** explícale que es el nombre de su tienda en internet y que lo más simple es comprarlo **dentro de Shopify** (Configuración → Dominios → Comprar dominio), porque así se conecta solo. Consejos: corto, fácil de decir, sin guiones, preferiblemente .com. Él lo compra. Si no quiere comprarlo todavía, sigue sin dominio: se puede hacer el jueves.
3. **Node.js:** revisa si lo tiene con `node --version`. Si no:
   - Mac: si tiene Homebrew (`brew --version`), instálalo con `brew install node`. Si no, que lo descargue de https://nodejs.org (botón LTS), lo instale como cualquier programa y vuelva a abrir la terminal.
   - Windows: `winget install OpenJS.NodeJS.LTS`. Después que cierre y vuelva a abrir PowerShell y Claude.
4. **Shopify CLI:** instálala con `npm install -g @shopify/cli@latest` y revisa con `shopify version` que sea 3.93 o más nueva.
5. **Conectar la tienda con Claude:** corre
   `shopify store auth --store SU-TIENDA.myshopify.com --scopes read_products,write_products,read_files,write_files,read_themes,write_themes,read_content,write_content,read_online_store_pages,write_online_store_pages,read_online_store_navigation,write_online_store_navigation,read_legal_policies,write_legal_policies,read_shipping,write_shipping,read_discounts,write_discounts`
   Se abre el navegador: que inicie sesión y acepte. Si algún permiso da error, quítalo de la lista y vuelve a correr.
6. **Prueba:** corre `shopify store execute --store SU-TIENDA.myshopify.com --query 'query { shop { name } }'`. Si responde con el nombre de su tienda, quedó conectada.
7. Anota en `perfil.md` qué quedó listo. Dile: "Tu tienda está conectada con Claude. Mañana la montamos con la skill de tienda".

## Etapa 3 · Jueves en la noche: Meta y Higgsfield
Explícale primero por qué se hace con calma: Meta es estricto con las cuentas nuevas y un error puede bloquearla.
1. **Perfil de Facebook:** que use su perfil personal real, no uno nuevo, y active la autenticación en dos pasos (Configuración → Centro de cuentas → Contraseña y seguridad).
2. **Portafolio comercial** (antes Business Manager): crearlo en https://business.facebook.com con su nombre y el de su tienda.
3. **Cuenta publicitaria:** dentro del portafolio, en Configuración → Cuentas → Cuentas publicitarias. **Antes de crearla**, que elija bien la moneda (la de su tarjeta) y la zona horaria (la de su país), porque no se pueden cambiar después.
4. **Método de pago:** una tarjeta que acepte cobros internacionales. Lo pone él.
5. **Conectar Shopify con Meta:** en Shopify, instalar la app "Facebook & Instagram" (de Meta), conectar su portafolio, su cuenta publicitaria y su página, y aceptar compartir datos. Eso crea el píxel que avisa cada compra.
6. **Verificar el dominio** en el portafolio (Configuración → Seguridad de la marca → Dominios). Si compró el dominio en Shopify, la opción más simple es la etiqueta meta: copia la etiqueta que da Meta y, si la tienda está conectada, ofrécele agregarla al tema por él.
7. **Higgsfield:** que cree su cuenta con el link del reto y elija el plan más básico con créditos (el gratis no trae créditos). Después, conectar Higgsfield a Claude: que entre a https://claude.ai/customize/connectors, busque Higgsfield y lo conecte. Luego, dentro de Claude, que escriba `/mcp` para comprobar que aparece. Si no aparece en la lista de conectores, dile que lo resolvemos en la clase del viernes.

**Errores que bloquean cuentas, díselos en voz alta:** crear un perfil nuevo para anunciar, crear varias cuentas publicitarias seguidas, cambiar datos muchas veces, usar una tarjeta que rechaza cobros internacionales.

Si Meta le pide verificación o le bloquea algo, tranquilízalo: la tarea del viernes cuenta igual con la campaña armada.

## Al terminar cualquier etapa
Dale un resumen corto de lo que quedó listo, lo que falta y cuándo se usa. Actualiza `perfil.md` con una sección "Herramientas" con cada cosa marcada como lista o pendiente.
