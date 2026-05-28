#1. Registrar producto → pide nombre y precio, los acumula
# 2. Ver resumen → muestra total y cantidad
# 3. Salir
total = 0
cantidad = 0
while True:
    print("1.- Registrar producto")
    print("2.- Ver resumen")
    print("3.- Salir")

    while True:
        try:
            op = int(input("Opcion:(1-3)"))
            break
        except ValueError:
            print("Solo numeros enteros")

    if op == 1:
        while True:
            nombre = input("Nombre del producto: ").upper().replace(" ", "")
            if len(nombre) >= 4:
                break
            print("Minimo 4 letras y sin espacios")

        while True:
            try:
                precio = int(input("Precio: "))
                if precio > 0:
                    break
                print("El precio debe ser mayor a 0")
            except:
                print("Solo numeros enteros")

        total += precio
        cantidad += 1
        print(f"Producto: {nombre} registrado")
    elif op == 2:
        print(f"Productos registrados: {cantidad}")
        print(f"Total acumulado: {total}")
    elif op == 3:
        print("Hasta luego")
        break
    else:
        print("Opcion invalida")    
