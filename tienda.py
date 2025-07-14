#Módulo 1: Bienvenida.
def bienvenida():
    print("Bienvenid@ a la tiendita escolar")
    nombre = input("¿Cuál es tu nombre? ")
    return nombre

#Módulo 2: Menú de productos.
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

#Módulo 3: Compras.
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

#Módulo 4: Pagos.
def procesar_pago(carrito):
    total = 0
    print("\nCalculando el total...")

    for producto, (cantidad, precio) in carrito.items():
        total += cantidad * precio
    print(f"\nTotal a pagar: ${total}") 

    while True:
        try:
            pago = float(input("Ingresa la cantidad con la que vas a pagar: $"))
       
            if pago < total:
                print("Monto insuficiente. Intenta de nuevo.")
            else:
                cambio = pago - total 
                print(f"Pago recibido: ${pago}")
                print(f"Cambio: ${round(cambio, 2)}")
                return total, pago, round(cambio, 2) 
        except ValueError:
            print("Entrada inválida. Ingresa un número válido.")

#Módulo 5: Ticket y cierre. 
