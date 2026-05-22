'''
█ Registro de juegos
Preguntar cuantos juegos son.
Debe preguntar al usuario Nombre del juego;
-Al menos 5 caracteres
-No debe incluir espacios y todas mayúsculas
Preguntar precio
-Solo números enteros positivos
-Si vale mas de 20000 es Indie pero menos de 40000
-Si vale 40000 o mas, es de Estudio 
-Mostar al final cuantos hay de cada categoría
Clasificación ( debe preguntar la edad objetiva)
- E para todos (<12)
- +12 para adolescentes (12 y 17)
- M para personas de mas de 18 (+18)
-MOSTRAR RESUMEN
EJ: Hay 4 indies, y 5 de estudio. Solo 3 son clasificación E
Uso de try- except obligatorio
'''


indie=0
estudio=0
tod=0
adol=0
mayo=0

while True:
    try:
        juegos=int(input("Cuantos juegos se registraran? "))
        break
    except ValueError as er:
        print("Numero de juegos invalido. Error", er)

for i in range (juegos):
    titulo=input("Ingrese el nombre del juego (Al menos 5 caracteres y sin espacios): ").upper()
    titulo=titulo.replace(" ", "")
    while " " in titulo or len(titulo)<5:
        print("No de incluir espacios")
        titulo=input("Ingrese el nombre del juego (Al menos 5 caracteres y sin espacios): ").upper()

    while len(titulo)<5:
        print("El titulo es muy corto")
        titulo=input("Ingrese el nombre del juego (Al menos 5 caracteres y sin espacios): ").upper()

    while True:
        try:
            precio=int(input("Ingrese el precio del juego: "))
            if precio>=20000 and precio<40000:
                print("El juego es indie")
                indie+=1
                break
            elif precio>=40000:
                print("El juego es de estudio")
                estudio+=1
                break
            else:
                print("El precio no puede ser menor a 20.000") 
        except:
            print("Solo numeros enteros positivos")

    

    while True:
        try:
            clasif=int(input("Ingrese la clacificacion del juego (edad): "))
            break
        except:
            print("Solo numeros enteros positivos")
    
    if clasif<=12:
        print("El juego es de todo publico")
        tod+=1
    elif clasif>12 and clasif<17:
        print("El juego es para adolescentes")
        adol+=1
    elif clasif>=18:
        print("El juego es para mayores")
        mayo+=1

print(f"hay {indie} juegos indie y {estudio} juegos de estudios")
print(f"Tambien hay {tod} juegos de todas las edades , {adol} juegos para adolecentes y {mayo} juegos para mayores")


'''
El programa debe tener un menú de opciones de donde se pueda realizar el pago del cupo de la tarjeta de crédito, como también simular nuevas compras, y estas una vez sumadas se resten al cupo disponible. 
Las opciones disponibles deben estar construidas de la siguiente forma:
1.	Pago de Tarjeta de Crédito:
a.	El usuario comienza con una deuda de $100.000
b.	El usuario puede ingresar un monto para realizar un pago en la tarje-ta de crédito.
c.	Se debe verificar que el monto ingresado sea mayor o igual a cero.
d.	Se debe verificar que el monto a pagar no exceda la deuda actual de la tarjeta.
e.	Al pagar el sistema debe descontar de la deuda total
f.	Si las verificaciones son exitosas, se realiza el pago y se actualiza el saldo de la tarjeta.
2.	Simulación de Compras:
a.	El usuario puede simular realizar un número ilimitado de compras.
b.	Para cada compra, se solicita al usuario ingresar el monto de la compra. El programa suma los montos de cada compra. 
c.	Se verifica que el monto de la compra sea mayor o igual a cero.
d.	Se realiza la compra y se actualiza el saldo de la tarjeta para cada iteración del bucle for.
3.	Salir:
a.	Al seleccionar esta opción, el programa debe cerrarse o finalizar.

A considerar:
1.	Manejo de Errores:
a.	Se utilizan bloques try y except para manejar posibles errores al in-gresar datos, validar valores no numéricos y errores inesperados. 
b.	Se debe programar mensajes de error específicos para guiar al usuario sobre posibles problemas.
Avtividad en el AVA 2.5.3
'''

deuda=-100000
op=0
subop1=0
while op!=4:
    try:
     print("1.-Tarjeta de credito")
     print("2.-Comprar")
     print("3.-Cupo disponible")
     print("4.-Salir")
     op=int(input("Escoger una opcion (1-4): "))

     if op==1:
        print("1.-realizar pago a la tarjeta")
        print("2.-salir")
        subop1=int(input("ingrese opcion:"))
        while subop1!=2:
            try:
                if subop1==1:
                 suma=int(input("cuanto desea agregar a la tarjeta: "))
                 while suma>deuda:
                     print("No puede pagar mas de lo que debe!")
                     suma=int(input("cuanto desea agregar a la tarjeta: "))
                 
                 break
            except ValueError:
                print("Debe ser un numero mayor que 0")
                break
     elif op==2:
        valor=int(input("ingrese el valor de la compra: "))
        if valor<deuda:
           print("compra realizada con exito")
        else:
           print("saldo insuficiente por favor revise su saldo disponible")
     elif op==3:
        print("su saldo actualmente es de:", deuda)
    
    except ValueError:
     print("Debe ingresar un numero entre 1 y 4")

#solucion 2


deuda = 100000
op = 0

while op != 3:
    print("1.- Pagar deudas")
    print("2.- Comprar")
    print("3.- Salir")
    while True:
        try:
            op = int(input("Ingrese su opcion: "))
            break
        except ValueError as er:
            print("Solo numeros enteros y positivos")

    match op:
        case 1:
            print(f"El monto total de la deuda es de {deuda}")
            while True:
                try:
                    monto = int(input("Ingrese el monto a pagar: "))
                    break
                except:
                    print("Solo numeros enteros y positivos")
                
            if monto >= 0 and monto <= deuda:
                deuda -= monto
                print(f"El total actual de la deuda es: {deuda}")
            else:
                print("El monto debe ser mayor a 0 y menor o igual a la deuda a pagar")

        case 2:
            while True:
                try:
                    compras = int(input("Ingrese la cantidad de compras: "))
                    break
                except:
                    print("Solo numeros enteros y positivos")
            for i in range(compras):
                while True:
                    try:
                        monto = int(input("Ingrese el monto de la compra: "))
                        break
                    except:
                        print("Solo numeros enteros y positivos")
                if monto >= 0:
                    deuda += monto
                else:
                    print("El pago debe ser mayor a 0")
        
        case 3:
            print("Saliendo del sistema")