while True:
    try:
        edad=int(input("Ingrese su edad: ")) # si aparece un error, 
        # salta a la linea 6, donde esta except para manejar el error
        print("Su edad es", edad)
        break
    except ValueError as valordelError:
        print("Solo se aceptan numeros enteros")
        print(valordelError)

edad=int(input("Ingrese su edad: "))


for i in range(10):
    n1=int(input("Ingrese un numero: "))
    if n1%2!=0:
        break

# ingrese nuemros indefinidamente 
# hasta que ponga el numero 0.
# Sumelos y muestre el total.
num=0
while True:
    try:
        n1=int(input("Ingrese un numero: "))
        num+=n1
        if n1==0:
            break
    except:
        print("SOlo numeros enteros")

print("EL total es" , num)

# Ejempo de menu con 
# try except

op=0
total=0
cantPRod=0
while op!=4:
    try:
        print("1.- Radio sterero Sony $70.000")
        print("2.- LGTV 55 pulgadas Super gamer $500.000 ")
        print("3.- PS5 $580.000")
        print("4.- Salir")
        print("Seleccione una opcion")
        op=int(input())

        match op:
            case 1:
                print("El precio a pagar es ", 70000*1.19)
                total+=70000*1.19
                cantPRod+=1
            case 2:
                print("El precio a pagar es ", 500000*1.19)
                total+=500000*1.19
                cantPRod+=1
            case 3:
                print("El precio a pagar es ", 580000*1.19)
                total+=580000*1.19
                cantPRod+=1
            case 4:
                print(f"Su total a pagar es {total}")
                print(f"La cantidad de articulos es {cantPRod}")
            case _:
                print("Opcion Inválida")  # opcion por defecto
    except :
        print("Debe ingresar solo numeros enteros")

porc=float(input("Ingrese el porcetaje de rucos en su comuna"))

if porc>0 and porc<100:
    print("Porcentaje correcto")
else:
    print("Porcentaje fuera de rango")


# validacion de pasajes y manejo de error

totalIngresos=0
pasaje=int(input("Ingrese la cantidad de pasajes que quiere vender: "))
for i in range(pasaje):
    while True:
        try:
            monto=int(input("Ingrese el Valor de cada pasaje: "))
            break
        except:
            print("Dato No Valido, ingeressar un nuemro entero positivo")
            
    totalIngresos+=monto
   
print(f"Monto {totalIngresos}")
print(f"Por la cantidad de {pasaje} entradas")


toon1=input("Ingrese el toon 1: ")
toon2=input("Ingrese el toon 2: ")

v1=0
v2=0
while True:
    try:
        cant=int(input("Cauntos votantes son? "))
        break
    except:
        print( " Solo puede ingresar valores enteros positivos")
while cant>0:
    # pedir votos
    while True:
        try:
            voto=int(input(f"Por quien votará? 1.- {toon1} 2.- {toon2}: "))
            break
        except ValueError as r:
            print( " Solo puede ingresar valores enteros positivos")
    if voto==1:
        v1+=1
    elif voto==2:
        v2+=1
    else:
        print("Voto nulo")
    cant-=1

if v1>v2:
    print(f"Gano {toon1} con {v1} votos")
elif v2>v1:
    print(f"Gano {toon2} con {v2} votos")
else:
    print("Fue un empate")

# Preguntar el codigo de descuento de una entrada a un concierto
# validar que los folios esten entre 7.000 y 21.000
# Preguntar si esa en cancha vip, cancha general, o tribuna
# Cada entrada vale 40000, pero los impuestos son
# vip * 1.8, genral, 1.4, y tibuna 1.2
# Mostrar el valor a pagar al final 
# poner manejo de error ára poder solucionarlo

