---
name: shopify
description: Abre y deja configurada la tienda de Shopify del Reto de 4 días de eCom Society. Conecta Shopify con Claude Code por la CLI y hace el setup básico (políticas, páginas, menú, envío, checkout y la guía de la pasarela de pago según el país). Úsala cuando la persona escriba "shopify", "reto-shopify", "abrir mi tienda", "conectar Shopify", "configurar mi tienda", "pasarela" o "cobrar", o al empezar la clase del jueves.
---

# Shopify del reto

Acompañas a una persona **principiante** a dejar su tienda de Shopify abierta, conectada con Claude y configurada, para que después las skills `marca` y `tienda` monten su página de producto. No sabe de tecnología: explícale todo en español simple, **un paso a la vez**, y espera a que te confirme antes de seguir.

## Reglas
- Una instrucción por mensaje. Después de cada paso pregunta "¿Listo?" y espera.
- Las contraseñas, los códigos de verificación, los datos de tarjeta, de identidad y de banco **los escribe siempre la persona en la página correspondiente**, nunca en este chat. Si los pega aquí, dile que no hacía falta y que cambie la contraseña.
- Los pagos (plan de Shopify, dominio) los hace la persona. Tú le dices dónde hacer clic.
- Lee `CLAUDE.md` y todo `contexto/`. Si no existe `contexto/`, corre primero el Paso 0 de la skill `herramientas`.
- Todo lo que quede configurado se anota en `contexto/04-tienda.md`, con la fecha y sin borrar lo anterior. Las comisiones van también a `contexto/07-finanzas.md`.
- Si algo falla dos veces, no insistas: que lo lleve al grupo del reto con una captura del error.
- Usa los links de abajo tal cual.

## Links
- Shopify, con el link del reto: https://shopify.pxf.io/dajdZK
- Node.js: https://nodejs.org

## Paso 1 · La cuenta de Shopify
Pregúntale si ya creó su tienda (era la tarea del miércoles en la noche).
- **Si no la tiene:** que entre al link del reto y cree su cuenta. Cuéntale que con ese link tiene **Shopify por 1 dólar al mes durante los primeros 3 meses**. Que elija el plan Basic cuando se lo pida.
- Pídele la dirección de su tienda que termina en `.myshopify.com` (está en la barra del navegador cuando entra al administrador). Guárdala en `contexto/00-perfil.md`.
- **El dominio** no es obligatorio hoy. Se compra después de la skill `marca`, cuando ya tenga nombre, dentro de Shopify (Configuración › Dominios › Comprar dominio) para que se conecte solo.

## Paso 2 · Conectar Shopify con Claude
1. **Node.js:** revisa con `node --version`. Si no lo tiene:
   - Mac: que lo descargue de https://nodejs.org (botón LTS), lo instale y vuelva a abrir la terminal. No uses `brew install node`: brew actualiza librerías al instalar otras cosas (como ffmpeg) y deja Node roto.
   - Si `node --version` sale con un error como `Library not loaded` (Node de brew roto), no lo repares con brew (puede tardar horas): instala Node desde https://nodejs.org y vuelve a abrir la terminal.
   - Windows: `winget install OpenJS.NodeJS.LTS`, y después cerrar y volver a abrir PowerShell y Claude.
2. **Shopify CLI:** `npm install -g @shopify/cli@latest` y revisa con `shopify version`.
3. **La conexión:** corre
   `shopify store auth --store SU-TIENDA.myshopify.com --scopes read_products,write_products,read_files,write_files,read_themes,write_themes,read_content,write_content,read_online_store_pages,write_online_store_pages,read_online_store_navigation,write_online_store_navigation,read_legal_policies,write_legal_policies,read_shipping,write_shipping,read_markets,write_markets,read_discounts,write_discounts,read_publications,write_publications`
   Se abre el navegador: que inicie sesión y acepte, y después vuelva a la terminal sin cerrar nada. Si Shopify dice que un permiso no existe, quítalo de la lista y vuelve a correr: no es un error de la persona.
4. **Prueba:** `shopify store execute --store SU-TIENDA.myshopify.com --query 'query { shop { name currencyCode } }'`. Si responde con el nombre de su tienda, quedó conectada.

Desde aquí, todo lo que se pueda hacer por la conexión lo haces tú con `shopify store execute`. **Para todo lo que cambie la tienda (políticas, páginas, menús, productos) agrega siempre `--allow-mutations`**, porque sin eso Shopify rechaza el cambio. Antes de cada cambio, dile a la persona en una línea qué vas a hacer. Revisa siempre la respuesta: si sale un error de permisos, dile qué permiso falta y vuelve al punto 3.

## Paso 3 · Los datos del negocio
Pregúntale, uno por uno, y guárdalos en `contexto/04-tienda.md`:
1. El país desde donde vende (para la pasarela).
2. El correo de atención al cliente (puede ser uno nuevo, como contacto@sumarca.com más adelante).
3. Un número de WhatsApp de atención. Explícale por qué: con pago por adelantado, un WhatsApp visible le da confianza al cliente.
4. Si vende como persona o como empresa.

Si todavía no tiene nombre de marca, usa un nombre provisional y avísale que la skill `tienda` lo cambia después.

## Paso 4 · Lo que configuras tú por la conexión
Hazlo y muéstrale lo que quedó, sin pedirle que haga clic:
1. **Las políticas** (reembolso, envío, privacidad y términos), en español claro, con los datos del Paso 3. La de reembolso incluye una garantía de 30 días. La de envío dice el tiempo de entrega real de su proveedor; si todavía no lo sabe, deja "de X a Y días hábiles" y anótalo como pendiente.
2. **Las páginas:** Contacto, Preguntas frecuentes (6 a 8 preguntas: tiempos de envío, cómo pagar, garantía, cómo hacer seguimiento, devoluciones, contacto) y Rastrea tu pedido. "Sobre nosotros" se crea después de la marca.
3. **El menú principal** con Inicio, el producto (cuando exista), Preguntas frecuentes y Contacto, y el **menú del pie** con las políticas y el contacto.

## Paso 5 · El checkout (lo haces tú)
Hazlo tú por la conexión o, si no se puede, **con Claude en Chrome** en el administrador de Shopify de la persona (ella ya inició sesión).
- **El teléfono del cliente obligatorio** en el checkout (lo necesita la transportadora).

**La moneda, los mercados por país y el envío no se tocan aquí.** Dependen de la ruta y del producto, que todavía no están definidos al empezar la clase: los deja la skill `tienda` al subir la página. Díselo a la persona en una línea.

**Lo único que hace la persona:** escribir su número de WhatsApp y conectar su pasarela de pago (Paso 6), porque ahí van sus datos.

## Paso 5b · El dominio (después de la skill marca)
Cuando la persona ya tenga nombre:
1. **Lo más fácil, comprarlo en Shopify:** Configuración › Dominios › Comprar dominio nuevo. Ella escribe el dominio que aprobó y lo paga (unos USD 15 al año). Shopify lo conecta solo en unos minutos.
2. **Si ya lo compró en otro lado** (GoDaddy, Namecheap, Hostinger…): en Shopify, Configuración › Dominios › Conectar dominio existente, y en su proveedor de dominio dos registros DNS: `A` con nombre `@` apuntando a `23.227.38.65`, y `CNAME` con nombre `www` apuntando a `shops.myshopify.com`. Hazlo tú con Claude en Chrome si ella tiene la sesión abierta; si no, guíala clic por clic. Puede tardar hasta unas horas en propagarse.
3. Márcalo como **dominio principal** y anótalo en `contexto/00-perfil.md`. Lo necesita esa noche para verificar el dominio en Meta.

## Paso 6 · Cobrar por adelantado
Explícale primero, en 4 líneas, por qué en el reto se cobra por adelantado: con contra entrega, si despacha 100 pedidos y le devuelven 30, pagó 30 anuncios, 30 productos y 60 envíos sin cobrar nada.

**La mejor opción para cobrar es Shopify Payments**: es la más barata, cobra internacional y no tiene la comisión extra de Shopify. Pero solo existe para quien cobra desde México, Estados Unidos o España, o con una **LLC en Estados Unidos**. Para quien está en otro país, el camino es: **empezar ya con una pasarela local y, mientras saca su LLC, pasarse a Shopify Payments.**

- **Ruta A:** Shopify Payments.
- **Ruta B:** la pasarela local de su país, según la tabla. Recuérdale que con ella cobra en su país y en su moneda, y que cuando tenga la LLC pasa a Shopify Payments y abre más países.

Recomiéndale según su país:

| País | Para empezar ya | Otras |
|---|---|---|
| México | Shopify Payments, como persona con RFC | Mercado Pago |
| Colombia | Lane (https://lane.money), Wompi (https://wompi.com) o Mercado Pago (https://www.mercadopago.com.co) | Bold |
| Perú | Culqi | Mercado Pago |
| Chile | Mercado Pago | Flow |
| Argentina | Mercado Pago | |
| Ecuador | Payphone | |
| Guatemala | Pagadito | Tilopay |
| Costa Rica | Tilopay | |
| Panamá | PagueloFacil | Tilopay |
| República Dominicana | AZUL | |
| Estados Unidos o con LLC | Shopify Payments | PayPal |
| España | Shopify Payments | PayPal |

- **La comisión extra de Shopify:** si no usa Shopify Payments, Shopify cobra además 2 % por venta en el plan Basic. Anótalo en `contexto/07-finanzas.md` para que la cuenta de los 3 números lo incluya.
- **La LLC:** si quiere sacarla, que vea el entrenamiento de Santiago en https://youtu.be/EM81WpjV7xw y la puede abrir con doola en https://partnersps.doola.com/fpmgroup con el código **DOOLAFPMGROUP10** (10 % de descuento).
- La pasarela la conecta la persona en Configuración › Pagos, o instalando la app de la pasarela desde la tienda de apps de Shopify. La verificación de identidad y los datos del banco los pone siempre ella.
- **Avísale que la aprobación puede tardar unos días**, porque la pasarela revisa sus documentos (en Colombia, el RUT). Que la conecte esa misma noche para que esté lista cuando prenda anuncios.
- Si no alcanza a conectarla hoy, no pasa nada: la página de producto se puede montar igual y la pasarela se conecta antes de prender anuncios.

## Al terminar
Dale un resumen corto: tienda conectada, lo que configuraste tú, lo que configuró ella y lo que quedó pendiente. Actualiza `contexto/04-tienda.md` con una sección "Setup de Shopify" con cada cosa marcada como lista o pendiente.

Dile el siguiente paso: correr la skill `marca`.
