while True:
    try:
        num = int(input("Cuantos pasajes desea vender: "))
        break
    except:
         print("Solo numeros enteros")
TotalIngresos=0        
for i in range(num):
    while True:
        try:
            precio=input(f"Ingrese el precio del pasaje {i+1}: ")
            TotalIngresos+=TotalIngresos
            break
        except ValueError as e:
            print("Solo numeros enteros.Error:", e)

print("El total valor a pagar es ", TotalIngresos)
