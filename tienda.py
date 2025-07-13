#Modulo 1
def bienvenida():
    print("Bienvenid@ a la tiendita escolar")
    nombre = input("¿Cuál es tu nombre? ")
    return nombre

#Modulo 2
def mostrar_productos():
    productos = {
        1: ("Galletas", 10),
        2: ("Jugos", 15),
        3: ("Chocolates", 20),
        4: ("Chicles", 5),
        5: ("Papas", 8),
        6: ("Agua", 12)
    }

    print("\n Menu de Productos:")
    for clave, (nombre, precio) in productos.items():
        print(f"{clave}. {nombre} - ${precio}")
    return productos

#Modulo 3
def realizar_compra():
    productos = mostrar_productos()
    carrito = {}

    while True:
        try:
            opcion = int(input("\nIngresa el número del producto que quieres comprar (0 para finalizar): "))
            
            if opcion == 0:
                break

            if opcion not in productos:
                print("Producto no válido. Intenta de nuevo.")
                continue

            cantidad = int(input(f"¿Cuántos {productos[opcion][0]} quieres comprar? "))
            
            if cantidad <= 0:
                print("Cantidad no válida.")
                continue

            nombre_producto, precio = productos[opcion]

            if nombre_producto in carrito:
                carrito[nombre_producto] = (
                    carrito[nombre_producto][0] + cantidad,
                    precio
                )
            else:
                carrito[nombre_producto] = (cantidad, precio)

            print(f"{cantidad} {nombre_producto} agregado(s) al carrito.")

        except ValueError:
            print("Entrada inválida. Ingresa solo números.")
    
    if not carrito:
        print("No seleccionaste ningún producto.")
    else:
        print("\nResumen de tu carrito:")
        for producto, (cantidad, precio) in carrito.items():
            print(f"{producto}: {cantidad} x ${precio} = ${cantidad * precio}")

    return carrito