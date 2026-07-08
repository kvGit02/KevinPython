# ==========================
# DICCIONARIOS
# ==========================

productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['Lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'Integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['Lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'Integrada'],
    '342FHD': ['Lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']
}

stock = {
    '8475HD': [387990,10],
    '2175HD': [327990,4],
    'JjfFHD': [424990,1],
    'fgdxFHD': [664990,21],
    '123FHD': [290890,32],
    '342FHD': [444990,7],
    'GF75HD': [749990,2],
    'UWU131HD': [349990,1]
}

# ==========================
# OPCIÓN 1
# ==========================

def stock_marca(marca):

    total = 0

    for modelo, datos in productos.items():

        if datos[0].lower() == marca.lower():

            total += stock[modelo][1]

    print("El stock es:", total)

# ==========================
# OPCIÓN 2
# ==========================

def busqueda_precio(p_min, p_max):

    lista = []

    for modelo, datos in stock.items():

        precio = datos[0]
        cantidad = datos[1]

        if p_min <= precio <= p_max and cantidad > 0:

            marca = productos[modelo][0]

            lista.append(f"{marca}--{modelo}")

    if len(lista) > 0:

        lista.sort()

        print("Los notebooks encontrados son:")

        print(lista)

    else:

        print("No hay notebooks en ese rango de precios.")

# ==========================
# OPCIÓN 3
# ==========================

def actualizar_precio(modelo, p):

    if modelo in stock:

        stock[modelo][0] = p

        return True

    else:

        return False

# ==========================
# MENÚ PRINCIPAL
# ==========================

def menu():

    while True:

        print("\n*** MENU PRINCIPAL ***")
        print("1. Stock marca")
        print("2. Búsqueda por precio")
        print("3. Actualizar precio")
        print("4. Salir")

        op = input("Ingrese opción: ")

        match op:

            case "1":

                marca = input("Ingrese marca: ")

                stock_marca(marca)

            case "2":

                while True:

                    try:

                        minimo = int(input("Ingrese precio mínimo: "))
                        maximo = int(input("Ingrese precio máximo: "))

                        busqueda_precio(minimo, maximo)

                        break

                    except:

                        print("Debe ingresar valores enteros!!")

            case "3":

                while True:

                    modelo = input("Ingrese modelo: ")

                    precio = int(input("Ingrese precio nuevo: "))

                    if actualizar_precio(modelo, precio):

                        print("Precio actualizado!!")

                    else:

                        print("El modelo no existe!!")

                    seguir = input("¿Desea actualizar otro precio (si/no)? ")

                    if seguir.lower() == "no":

                        break

            case "4":

                print("Programa finalizado.")

                break

            case _:

                print("Debe seleccionar una opción válida!!")

menu()