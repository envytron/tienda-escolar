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
