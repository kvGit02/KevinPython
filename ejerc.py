cupos = 75
transacciones = 0
while True:
    print(f"cupos disponibles: {cupos}")
    print(f"transacciones hechas: {transacciones}")
    print("-----------------------")
    print("1.- Reservar cupos")
    print("2.- Cancelar Reserva")
    opcion = input("Seleccione una opcion")

    if opcion == 1:
        cantidad = int(input("Cuantos cupos desea rservar?: "))
        if cantidad > 0 and cantidad <= cupos:
            cupos -= cantidad
            transacciones += 1
            print(f"Reserva exitosa. Cupos restantes: {cupos}")
        else:
            print("Opcion invalida")
    elif opcion == 2:
        cantidad = int(input("Cuantos cupos deseas liberar?:"))
        if cantidad > 0 and (cupos+cantidad) <=75:
            cupos += cantidad
            transacciones -=1
            print(f"cancelacion exitosa. Cupos disponibles: {cupos}")
        else:
            print("Operacion invalida")
    elif opcion == 5:
        print("Gracias por utilizar nuestro programa, hasta la proxima")
        break