# #promedioNotas
# # Completar con las sentencias de código, que permitan realizar:
# # 1.- Agregar notas a la lista creada
# # 2.- Muestre por pantalla todas las notas ingresadas
# # 3.- Muestra la cantidad de notas ingresadas
# # 4.- Obtenga el promedio de las notas
# sw = 1
# listaNotas = []
# print("Presione 1 para ingresar sus notas")
# print("Presione cualquier tecla para salir")
# op=int(input("Seleccione opción"))
# if(op == 1):
#     while sw==1:
#         try:
#             print("----------------------------------------------------------")
#             nota=int(input("Incorpore su nota, si desea salir, presione 0: "))
#             if(nota != 0):
#                 listaNotas.append(nota)
#                 print("Notas ingresadas: ", listaNotas)
#                 print("Cantidad de notas ingresadas: ", len(listaNotas))
#                 print("Promedio de las notas: ", promedio_lista(listaNotas))
#             else:
#                 print("Adiós")
#                 sw=0
#         except:
#             print("Ingreso Erróneo")
# else:
#     print("Adiós")

# Ejercicio 1: Suma de números pares
# Enunciado: Dada una lista de números enteros llamada numeros, calcula la suma de
# todos los números pares presentes en la lista utilizando un bucle.
# Python
# # Entrada de prueba
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Ejercicio 1: Suma de números pares
# Enunciado: Dada una lista de números enteros llamada numeros, calcula la suma de
# todos los números pares presentes en la lista utilizando un bucle.
# Python
# Entrada de prueba
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
suma_pares = 0
for numero in numeros:
    if numero % 2 == 0:
        suma_pares += numero
print("La suma de los números pares es:", suma_pares)


# Ejercicio 2: Contador de frecuencias de caracteres
# Enunciado: Dada una cadena de texto llamada texto, crea un diccionario llamado
# frecuencias donde las claves sean los caracteres y los valores sean la cantidad de
# veces que aparece cada carácter en el texto.
# Python
# Entrada de prueba
# texto = "programacion"
texto = "programacion"
frecuencias = {}
for caracter in texto:
    if caracter in frecuencias:
        frecuencias[caracter] += 1
    else:
        frecuencias[caracter] = 1
print("Frecuencias de caracteres:", frecuencias)