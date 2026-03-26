from modulo_servicios import agregar_producto, mostrar_inventario, calcu_estadisticas

inventario = []

#-----------------------------------
# Menú principal
#-----------------------------------    
running = True

while running :
    print("====MENÚ====")
    print("1. Agregar producto.")
    print("2. Mostrar inventario.")
    print("3. Calcular estadisticas.")
    print("4. Buscar producto.")
    print("5. Actualizar producto.")
    print("6. Eliminar producto.")
    print(". Salir")

    opcion = input("Seleccione una opción: \n")

    if opcion == "1":
        nombre = input("Ingrese nombre del producto: ")

        while True:
            try:
                precio = float(input("Ingrese el precio del producto: "))
                break
            except ValueError:
                print("Ingrese un precio valido.")

        while True:
            try:
                cantidad = int(input("Ingrese la cantidad del producto: "))   
                break
            except ValueError:
                print("Deberia ser un número.")     

        agregar_producto(inventario, nombre, precio, cantidad)
        print("\nProducto agregado exitosamente. \n")

    elif opcion == "2":
        mostrar_inventario(inventario)

    elif opcion == "3":
        calcu_estadisticas(inventario)

    elif opcion == "4":
        print("Saliendo del sistema...")
        running = False

    else:
        print("Ingrese una opción valida. intente nuevamente. \n")


# ----------------------------------------------------------------
# Este programa permite gestionar multiples productos en un inven
# tario.
# Se utiliza el menú interactvio con un bucle while para repetir
# opciones.
# Los productos se almacenan en una lista de diccionarios.
# Se aplican estructuras como:
# - Condicionales  (if, elif, else)
# - Bucles (While y for)
# - Funciones para  organizar el codigo
# Ademas, se pueden calcular estadisticas como el valor total y
# la cantidad total del productos. 
# ----------------------------------------------------------------



