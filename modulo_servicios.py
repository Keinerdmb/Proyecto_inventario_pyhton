def agregar_producto(inventario, nombre, precio, cantidad):
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    inventario.append(producto)

def mostrar_inventario(inventario):

#-----------------------------------
# Funcion (mostrar diccionario).
#-----------------------------------

    print("---Inventario---")

    if len (inventario) == 0:
        print("El inventario esta vacio. \n")

    else:
        for producto in inventario:
            print(f"Producto:{producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")
        print()

def calcu_estadisticas(inventario):

#-----------------------------------
# Funcion (calcular estadisticas).
#-----------------------------------

    print("---Estadisticas \n")

    if len(inventario) == 0:
        print("No hay productos registrados \n")
        return
    valor_total = 0
    total_productos = 0

    for producto in inventario:
        valor_total += producto ["precio"] * producto ["cantidad"]
        total_productos += producto ["cantidad"]

    print(f"Valor total del inventario {valor_total}")
    print(f"Productos totales: {total_productos}\n")
