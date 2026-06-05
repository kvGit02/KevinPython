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

# Ejercicio 3: Filtrar alumnos aprobados
# Enunciado: Tienes un diccionario llamado alumnos donde las claves son los nombres
# de los estudiantes y los valores son sus calificaciones. Crea una nueva lista llamada
# aprobados que contenga solo los nombres de los alumnos con una calificación mayor o
# igual a 6.0.
# Python
# Entrada de prueba
# alumnos = {"Ana": 7.5, "Luis": 5.0, "Pedro": 6.0, "María": 4.5,
# "Carlos": 8.2}
alumnos = {"Ana": 7.5, "Luis": 5.0, "Pedro": 6.0, "María": 4.5, "Carlos": 8.2}
aprobados = []
for nombre, calificacion in alumnos.items():
    if calificacion >= 6.0:
        aprobados.append(nombre)
print("Alumnos aprobados:", aprobados)


# Ejercicio 4: Combinar dos listas en un diccionario
# Enunciado: Dadas dos listas de la misma longitud, claves y valores, crea un
# diccionario llamado resultado que asocie cada elemento de la lista claves con el
# elemento correspondiente en la lista valores utilizando sus índices.
# Python
# # Entrada de prueba
# claves = ["nombre", "edad", "ciudad", "profesion"]
# valores = ["Carlos", 25, "Madrid", "Ingeniero"]}
claves = ["nombre", "edad", "ciudad", "profesion"]
valores = ["Carlos", 25, "Madrid", "Ingeniero"]
resultado = {}
for i in range(len(claves)):
    resultado[claves[i]] = valores[i]
print("Diccionario combinado:", resultado)
# Ejercicio 5: Encontrar el valor máximo y mínimo manualmente
# Enunciado: Dada una lista de números llamada valores, encuentra el número más
# grande y el más pequeño utilizando bucles y condicionales. No utilices las funciones
# integradas max() ni min().
# Python
# # Entrada de prueba
# valores = [34, 7, 23, 99, 5, 62, -2]
alumnos = {"Ana": 7.5, "Luis": 5.0, "Pedro": 6.0, "María": 4.5, "Carlos": 8.2}
aprobados = []
for nombre, calificacion in alumnos.items():
    if calificacion >= 6.0:
        aprobados.append(nombre)
print("Alumnos aprobados:", aprobados)
claves = ["nombre", "edad", "ciudad", "profesion"]
valores = ["Carlos", 25, "Madrid", "Ingeniero"]
resultado = {}
for i in range(len(claves)):
    resultado[claves[i]] = valores[i]
print("Diccionario combinado:", resultado)
valores = [34, 7, 23, 99, 5, 62, -2]
maximo = valores[0]
minimo = valores[0]
for valor in valores:
    if valor > maximo:
        maximo = valor
    if valor < minimo:
        minimo = valor
print("Valor máximo:", maximo)
print("Valor mínimo:", minimo)

# Ejercicio 6: Invertir un diccionario
# Enunciado: Dado un diccionario llamado original cuyos valores son únicos, crea un
# nuevo diccionario llamado invertido donde las claves sean los valores del diccionario
# original y los valores sean las claves originales.
# Python
# # Entrada de prueba
# original = {"a": 1, "b": 2, "c": 3, "d": 4}

original = {"a": 1, "b": 2, "c": 3, "d": 4}
invertido = {}
for clave, valor in original.items():
    invertido[valor] = clave
print("Diccionario invertido:", invertido)


# Ejercicio 7: Eliminar duplicados manteniendo el orden
# Enunciado: Dada una lista llamada elementos que contiene valores repetidos, crea una
# nueva lista llamada unicos que guarde los elementos sin repetir, asegurándote de
# mantener el orden original de su primera aparición.
# Python
# # Entrada de prueba
# elementos = [1, 2, 2, 3, 4, 4, 1, 5, 2, 6]

elementos = [1, 2, 2, 3, 4, 4, 1, 5, 2, 6]
unicos = []
for elemento in elementos:
    if elemento not in unicos:
        unicos.append(elemento)
print("Elementos únicos manteniendo el orden:", unicos)