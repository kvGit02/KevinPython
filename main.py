opcion = ""
while opcion != "3":
    print("\n--- COTIZADOR DE SEGUROS ---")
    print("1. Cotizar seguro")
    print("2. Ver tabla de aumentos")
    print("3. Salir")
    opcion = input("Opcion: ")

    if opcion == "1":
        valor_vehiculo = int(input("Valor del vehiculo: $"))
        if valor_vehiculo <= 0:
            print("Valor debe ser positivo.")
        else:
            edad = int(input("Edad del conductor: "))
            tipo = input("Tipo de seguro (A/B/C): ")
            # Convertir a mayúscula por si acaso
            if tipo == "a":
                tipo = "A"
            elif tipo == "b":
                tipo = "B"
            elif tipo == "c":
                tipo = "C"

            if tipo != "A" and tipo != "B" and tipo != "C":
                print("Tipo de seguro no valido. Debe ser A, B o C.")
            else:
                historial = input("Tiene historial de accidentes? (S/N): ")
                if historial == "s":
                    historial = "S"
                elif historial == "n":
                    historial = "N"

                if historial != "S" and historial != "N":
                    print("Historial debe ser S o N.")
                else:
                    # Cálculos
                    precio = valor_vehiculo * 0.03   # 3% base
                    print("Precio base (3% del valor): $" + str(int(precio)))

                    # 1. Tipo de seguro
                    if tipo == "A":
                        precio = precio * 1.15
                        print("+15% por tipo Amplio -> $" + str(int(precio)))
                    elif tipo == "B":
                        print("Tipo Limitado (sin cambio) -> $" + str(int(precio)))
                    elif tipo == "C":
                        precio = precio * 0.9
                        print("-10% por tipo Basico -> $" + str(int(precio)))

                    # 2. Edad
                    if edad < 25:
                        precio = precio * 1.20
                        print("+20% por edad menor a 25 -> $" + str(int(precio)))
                    elif edad >= 25 and edad <= 35:
                        precio = precio * 1.05
                        print("+5% por edad entre 25 y 35 -> $" + str(int(precio)))
                    elif edad > 65:
                        precio = precio * 1.10
                        print("+10% por edad mayor a 65 -> $" + str(int(precio)))
                    else:
                        print("Sin recargo por edad (36-65) -> $" + str(int(precio)))

                    # 3. Historial
                    if historial == "S":
                        precio = precio * 1.12
                        print("+12% por historial de accidentes -> $" + str(int(precio)))
                    else:
                        precio = precio * 0.95
                        print("-5% por buen historial -> $" + str(int(precio)))

                    print("--- PRECIO FINAL: $" + str(int(precio)) + " ---")

    elif opcion == "2":
        print("\nTabla de modificadores:")
        print("Tipo A: +15%")
        print("Tipo B: sin cambio")
        print("Tipo C: -10%")
        print("Edad <25: +20%")
        print("Edad 25-35: +5%")
        print("Edad 36-65: sin cambio")
        print("Edad >65: +10%")
        print("Con accidentes: +12%")
        print("Sin accidentes: -5%")
        print("Todos los cambios se aplican en cascada sobre el valor actual.")

    elif opcion != "3":
        print("Opcion incorrecta.")

print("Gracias por usar el cotizador.")

