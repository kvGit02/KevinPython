op=0
total=0
while op!=4:
    try:
        print("1.- PC $500.000")
        print("2.- LGTV 55 pulgadas $450.000")
        print("3.- Microondas Mademsa $100.000")
        print("4.- Salir")
        print("Seleccione una opcion")
        op=int(input())
        match op:
            case 1:
                print("El total a pagar es ",500000*1.19 )
                total+=500000*1.19
            case 2:
                print("El total a pagar es ",450000*1.19 )
                total+=450000*1.19
            case 3:
                print("El total a pagar es ",100000*1.19 )
                total+=100000*1.19
            case 4:
                print("Saliendo")
                print("El total a pagar es", total)
            case _:
                print("Opción inválida")
    except ValueError as e:
        print("Solo debe ingresar numeros enteros, Error",e)


# Calculadora

#  + - * /

# def suma():
#     n1=int(input("Ingrese un numero: "))
#     n2=int(input("Ingrese otro numero: "))
#     print(f"EL resultado es {n1+n2}")

# def resta():
#     n1=int(input("Ingrese un numero: "))
#     n2=int(input("Ingrese otro numero: "))
#     print(f"EL resultado es {n1-n2}")
# def multi():
#     n1=int(input("Ingrese un numero: "))
#     n2=int(input("Ingrese otro numero: "))
#     print(f"EL resultado es {n1*n2}")
# def divi():
#     n1=int(input("Ingrese un numero: "))
#     n2=int(input("Ingrese otro numero: "))
#     print(f"EL resultado es {n1/n2}")

# def calculadora():
#     op=0
#     while op!=5:
#         print("1.- suma")
#         print("2.- resta")
#         print("3.- Multiplicacion")
#         print("4.- Division")
#         print("5.- Salir")
#         print("Seleccione una opcion")
#         op=int(input())
#         match op:
#             case 1:
#                 suma()
#             case 2:
#                 resta()
#             case 3:
#                 multi()
#             case 4:
#                 divi()
#             case 5:
#                 print("Saliendo")
                
#             case _:
#                 print("Opción inválida")

# def tabla():
#     num=int(input("Ingrese un numero: "))

#     for i in range(10):
#         print(num, "x" , i+1 , "=", num*(i+1))
        

# def MultiProme():
#     notas=int(input("Ingrese la cant de notas: "))
#     suma=0
#     for i in range(notas):
#         n=float(input(f"Ingrese la nota {i+1}: "))
#         suma=suma+n
#     prom=suma/notas
#     print("El promedio es",round(prom,1) )

#     if prom>=4:
#         print("Alumno aprobado")
#     else:
#         print("Alumno reprobado")

# def programas():
#     op=0
#     while op!=4:
#         print('''
#         1.- MultiPRomedio
#         2.- Caluladora
#         3.- Tabla Multi
#         4.- Salir
#         ''')
#         op=int(input("Seleccione su opcion: "))
#         match op:
#             case 1:
#                 MultiProme()
#             case 2:
#                 calculadora()
#             case 3:
#                 tabla()
#             case 4:
#                 print("Saliendo")
                
#             case _:
#                 print("Opción inválida")

# programas()

# op=0
# cantPersonas=0 #contar la cant de personas que ingresan al zoo
# total=0 # total a pagar por las entradas
# while op!=4:
#     print('''
#         1.- Niño (1-17) $1.000
#         2.- Adulto (18-64) $3.000
#         3.- Adulto Mayor (64 o mas) $1.500
#         4.- Salir''')
#     op=int (input("Seleccione una opcion: "))
#     match op:
#         case 1:
#             #Preguntar cuantos son en cada persona
#             print("Pagando el precio de niño: ")
#             c=int(input("Cuantos son?: "))
#             # limitar la cant de personas de 1 a 10
#             while c<1 or c>10:
#                 print("Cantidad fuera d rango (1-10)")
#                 c=int(input("Cuantos son?: "))
#             total+=1000*c
#             cantPersonas+=c
#         case 2:
#             #Preguntar cuantos son en cada persona
#             print("Pagando el precio de adulto: ")
#             c=int(input("Cuantos son?: "))
#             # limitar la cant de personas de 1 a 10
#             while c<1 or c>10:
#                 print("Cantidad fuera d rango (1-10)")
#                 c=int(input("Cuantos son?: "))
#             total+=3000*c
#             cantPersonas+=c
#         case 3:
#             #Preguntar cuantos son en cada persona
#             print("Pagando el precio de anciano: ")
#             c=int(input("Cuantos son?: "))
#             # limitar la cant de personas de 1 a 10
#             while c<1 or c>10:
#                 print("Cantidad fuera d rango (1-10)")
#                 c=int(input("Cuantos son?: "))
#             total+=1500*c
#             cantPersonas+=c
#         case 4:
#             print("Saliendo")
#             print("El total a pagar es ", total)
#             print("La cantidad de personas es", cantPersonas)
#         case _:
#             print()



# Gererar un  codigo promocional de una entrada a un concierto
# que este entre 7.000 y 21.000
# Preguntar si esa en cancha vip, cancha general, o tribuna
# Cada entrada vale 40000, pero los impuestos son
# vip * 1.8, genral, 1.4, y tibuna 1.2

# Si el codigo promocional esta entre 7000 y 12000
# tiene un descuento del 10% sobre el precio final
# Mostrar el valor a pagar al final 

import random

codigo=random.randint(7000,21000)

print(f"tu codigo es {codigo}")

print("1.- VIP ")

print("2.- General ")

print("3.- Tribuna ")

op=int(input())



if op==1:
 print (f"el precio solo de la entrada es de {40000*1.8}")
 pf=40000*1.8
elif op==2:
 print (f"el precio solo de la entrada es de {40000*1.4}")
 pf=40000*1.4
elif op==3:
 print (f"el precio solo de la entrada es de {40000*1.2}")
 pf=40000*1.2
else:
 print ("entrada no valida")



if codigo>6999 or codigo<21001:

 pf=pf*0.9

print(f"el precio a pagar con el descuento será de {pf}")
