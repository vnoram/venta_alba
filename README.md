# Tienda Oficial Colo Colo

Este proyecto es una maqueta sencilla de un sitio de comercio electrónico para camisetas de Colo Colo. Consta de dos páginas estáticas escritas en HTML y estilizadas con CSS, con una pizca de JavaScript para simular el flujo de compra mediante `localStorage`.

## Estructura de archivos
- `index.html`: página de inicio y catálogo con tarjetas de producto.
- `carrito.html`: vista del carrito que muestra el detalle almacenado en el navegador.
- `style.css`: hoja de estilos compartida para ambas vistas.
- `img/`: carpeta con el logotipo y las imágenes de las camisetas.

## Flujo de navegación y carrito
1. **Catálogo (`index.html`)**
   - Cada producto incluye nombre, precio y botón **Agregar al carrito**.
   - El script obtiene el carrito desde `localStorage`, agrega el producto como un objeto `{ nombre, precio }` y vuelve a guardar la lista serializada.
   - Al agregar se muestra un `alert` indicando que el artículo se guardó y puede revisarse en la página del carrito.

2. **Carrito (`carrito.html`)**
   - Al cargar la página, se leen los datos guardados en `localStorage` y se renderiza una lista `<li>` con el nombre y el precio formateado (`toLocaleString('es-CL')`).
   - Si no hay elementos, se revela un mensaje "Tu carrito está vacío".
   - Se calcula el total sumando los precios, se muestra en la interfaz y se actualiza en cada renderizado.
   - El botón **Comprar Ahora** valida que exista al menos un producto; de lo contrario avisa con `alert`. Si hay artículos, muestra un mensaje de confirmación con el total simulado y luego limpia el carrito.

## Diseño y responsividad (`style.css`)
- Encabezado fijo con logotipo, navegación y un botón hamburguesa (`menu-toggle`) que alterna la clase `show` en la lista de enlaces para móviles.
- Uso de **CSS Grid** para acomodar las tarjetas de productos (`.productos`) con un mínimo de 220px por columna.
- Las tarjetas (`.producto`) incluyen sombras, bordes redondeados y animación al hacer hover.
- Botones y pie de página comparten la paleta negro/blanco del club.
- Media query a 600px ajusta la navegación en columna y muestra el toggler.

## Cómo funciona el JavaScript
- Ambos documentos definen funciones auxiliares idénticas:
  - `obtenerCarrito()`: intenta leer `carrito` desde `localStorage` y devuelve un arreglo vacío si no existe.
  - `guardarCarrito(carrito)`: persiste el arreglo serializado como JSON en `localStorage`.
- En `index.html`, cada botón usa `closest('.producto')` para encontrar su tarjeta, extrae el nombre, limpia el precio con una expresión regular y lo guarda.
- En `carrito.html`, la función `actualizarCarrito()` vuelve a generar la lista, muestra/oculta el mensaje vacío y mantiene actualizado el total.
- `toggleMenu()` se comparte en ambas páginas para manejar el menú responsive.

## Supuestos y limitaciones
- No hay backend: todo se ejecuta en el navegador y los datos se pierden al limpiar el almacenamiento local.
- No existe gestión de stock, cantidades ni autenticación; el carrito solo almacena un listado plano de productos seleccionados.
