#Pedir números indefinidamente hasta que el usuario ingrese 0. Mostrar la suma total, el mayor número ingresado y cuántos números ingresó.
total= 0
cantidad = 0
mayor = 0
while True:
    try:
        n = int(input("Ingrese un numero(0 para salir): "))
        if n == 0:
            break
        total += n
        cantidad += 1
        if n > mayor:
            mayor = n
    except ValueError:
        print("Solo numeros enteros")
print(f"Total: {total}")
print(f"Cantidad: {cantidad}")
print(f"Mayor: {mayor}")
