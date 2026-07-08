# ===============================
# BASE DE DATOS
# ===============================

productos = {
    "P001": ["Teclado", 25000, 10],
    "P002": ["Mouse", 15000, 8],
    "P003": ["Monitor", 120000, 4]
}

# ===============================
# MUESTRA TODOS LOS PRODUCTOS
# ===============================

def mostrarProductos(dic):

    print("\n===== PRODUCTOS =====")

    for codigo, datos in dic.items():

        print(f"Código : {codigo}")
        print(f"Nombre : {datos[0]}")
        print(f"Precio : ${datos[1]}")
        print(f"Stock  : {datos[2]}")
        print("-----------------------")

# ===============================
# BUSCAR POR NOMBRE
# ===============================

def buscarProducto(nombre):

    encontrado = False

    for codigo, datos in productos.items():

        if datos[0].lower() == nombre.lower():

            print(f"ID: {codigo}")
            print(datos)

            encontrado = True

    if encontrado == False:
        print("Producto no encontrado")

# ===============================
# AGREGAR PRODUCTO
# ===============================

def crearProducto(codigo, nombre, precio, stock):

    if codigo in productos:
        return False

    productos[codigo] = [nombre, precio, stock]

    return True

# ===============================
# ACTUALIZAR STOCK
# ===============================

def actualizarStock(codigo, stock):

    if codigo in productos:

        productos[codigo][2] = stock

        return True

    return False

# ===============================
# ELIMINAR PRODUCTO
# ===============================

def eliminarProducto(codigo):

    if codigo in productos:

        del productos[codigo]

        return True

    return False

# ===============================
# MOSTRAR SOLO LOS NOMBRES
# usando range(len())
# ===============================

def mostrarNombres():

    nombres = []

    for codigo, datos in productos.items():

        nombres.append(datos[0])

    print("\nLISTA DE NOMBRES")

    for i in range(len(nombres)):

        print(i, "-", nombres[i])

# ===============================
# PRODUCTOS POR PRECIO
# ===============================

def buscarPorPrecio(minimo, maximo):

    lista = []

    for codigo, datos in productos.items():

        precio = datos[1]

        if minimo <= precio <= maximo:

            lista.append(codigo)

    if len(lista) > 0:

        lista.sort()

        print(lista)

    else:

        print("No hay productos.")

# ===============================
# MENÚ
# ===============================

def menu():

    while True:

        print("\n========== MENÚ ==========")
        print("1. Mostrar productos")
        print("2. Agregar producto")
        print("3. Buscar producto")
        print("4. Actualizar stock")
        print("5. Eliminar producto")
        print("6. Mostrar nombres")
        print("7. Buscar por precio")
        print("8. Salir")

        opcion = int(input("Seleccione una opción: "))

        match opcion:

            case 1:

                mostrarProductos(productos)

            case 2:

                codigo = input("Código: ").upper()
                nombre = input("Nombre: ").strip()
                precio = int(input("Precio: "))
                stock = int(input("Stock: "))

                if crearProducto(codigo, nombre, precio, stock):
                    print("Producto agregado.")
                else:
                    print("Ese código ya existe.")

            case 3:

                nombre = input("Nombre: ")

                buscarProducto(nombre)

            case 4:

                codigo = input("Código: ").upper()
                stock = int(input("Nuevo stock: "))

                if actualizarStock(codigo, stock):
                    print("Actualizado correctamente.")
                else:
                    print("Código no encontrado.")

            case 5:

                codigo = input("Código: ").upper()

                if eliminarProducto(codigo):
                    print("Producto eliminado.")
                else:
                    print("Código no encontrado.")

            case 6:

                mostrarNombres()

            case 7:

                minimo = int(input("Precio mínimo: "))
                maximo = int(input("Precio máximo: "))

                buscarPorPrecio(minimo, maximo)

            case 8:

                print("Programa terminado.")
                break

            case _:

                print("Opción incorrecta.")

# ===============================
# INICIO DEL PROGRAMA
# ===============================

menu()