# ejemplo y uso de try except




# while True:
#     try:
#         num=int(input("Ingrese un numero: "))
#         break
#     except ValueError as er:
#         print("Solo numeros enteros")
#         print(er)
        
# '''sacar promedio'''
    
# print("Ingrese 3 notas")
# total=0
# for i in range (3):
#     while True:
#         try:
#             n=float(input(f"Ingrese la nota {i+1}: "))
#             break
#         except:
#             print("Se debe ingresar numeros decimales")
#     total+=n
# prom=total/3
# print(f"El promedio es {prom}")


# op=0
# total=0
# while op!=4:
#     try:
#         print("1.- PC $500.000")
#         print("2.- LGTV 55 pulgadas $450.000")
#         print("3.- Microondas Mademsa $100.000")
#         print("4.- Salir")
#         print("Seleccione una opcion")

#         op=int(input())
#         match op:
#             case 1:
#                 print("El total a pagar es ",500000*1.19 )
#                 total+=500000*1.19
#             case 2:
#                 print("El total a pagar es ",450000*1.19 )
#                 total+=450000*1.19
#             case 3:
#                 print("El total a pagar es ",100000*1.19 )
#                 total+=100000*1.19
#             case 4:
#                 print("Saliendo")
#                 print("El total a pagar es", total)
#             case _:
#                 print("Opción inválida")
#     except ValueError as e:
#         print("SOlo numeros enteros. Error: ", e)
'''
Deberás construir un programa que esta diseñado para ayudar en la venta de pasajes. 
Inicia preguntándote cuántos pasajes deseas vender. Luego, utiliza un proceso
 organizado (llamado bucle for) para pedirte el precio de cada pasaje por separado.
   Si ingresas un valor que no es un número, te indica que necesitas proporcionar 
   un valor numérico válido. Al final, muestra el monto total que se ha obtenido 
   por la venta de todos los pasajes
•	Solicita al usuario la cantidad de pasajes a vender.
•	Se utiliza un bucle for para iterar sobre la cantidad de pasajes.
•	Dentro del bucle, se solicita al usuario el precio de cada pasaje y 
se acumula en la variable totalIngresos.
•	Si el usuario ingresa un valor no numérico para el precio del pasaje, el programa 
muestra un mensaje y sale del bucle usando break.
•	Finalmente, se imprime el total de ingresos por la venta de pasajes
'''
# while True:
#     try:
#         cantP=int(input("Cuantos pasajes va a vender?"))
#         break
#     except Exception as e:
#         print("Solo valores enteros. Eror: ", e)
        
# totalIngresos=0
# for i in range(cantP):
#     while True:
#         try:
#             pasaje=int(input(f"Ingrese el precio del pasaje {i+1}: ")) 
#             totalIngresos+=pasaje
#             break
#         except ValueError as e:
#             print("Solo valores enteros. Eror: ", e)
# print(f"El total de los pasajes es {totalIngresos}")

'''Realiza construcción de un programa que deba realizar lo siguiente: 
Comienza con la inicialización de variables y solicita al usuario la 
cantidad de bultos. Luego, utiliza un bucle FOR para procesar cada
 bulto, solicitando el peso al usuario y manejando posibles errores
   (agregar excepciones). Dependiendo del peso ingresado, acumula valores
     y contadores correspondientes para bultos livianos y normales. 
     Finalmente, imprime el total a pagar por bultos livianos y normales,
       así como la cantidad de bultos en cada categoría
       blivi=1000
       normal=2000
'''

while True:
    try:
        cantP=int(input("Cuantos bultos son?"))
        break
    except Exception as e:
        print("Solo valores enteros. Eror: ", e)
bliviano=0
bnormales=0
for i in range(cantP):
    while True:
        try:
            bulto=float(input(f"Ingrese el peso del bulto {i+1} (en kg): ")) 
            if bulto <=5:
                bliviano+=1
            else:
                bnormales+=1
            break
        except ValueError as e:
            print("Solo valores decimales. Eror: ", e)



print(f"Bultos Livianos: {bliviano*1000}")
print(f"Bultos Normales: {bnormales*2000}")
print(f"El total a pagar es {bliviano*1000+bnormales*2000}")