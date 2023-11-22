# Definimos una lista para almacenar los productos.
# Es una lista de diccionarios

productos = []

# ----------------------------------------------------------
# Funciones para gestionar un arreglo con datos de productos
# ----------------------------------------------------------


def agregar_producto(codigo, descripcion, cantidad, precio, imagen, proveedor):

    # Parámetros:
    # - codigo: int, código numérico del producto.
    # - descripcion: str, descripción alfabética del producto.
    # - cantidad: int, cantidad en stock del producto.
    # - precio: float, precio de venta del producto.
    # - imagen: str, nombre de la imagen del producto.
    # - proveedor: int, número de proveedor del producto

    # Retorna:
    # - Valor booleano: True si el producto se agregó exitosamente al arreglo y False si ya existe un
    # producto con el mismo código y no se agrega el nuevo producto.

    nuevo_producto = {
        'codigo': codigo,
        'descripcion': descripcion,
        'cantidad': cantidad,
        'precio': precio,
        'imagen': imagen,
        'proveedor': proveedor
    }

    productos.append(nuevo_producto)
