
from random import randint
# Entrada del rango numérico
 
 
limite_inferior = int(input("Ingrese límite inferior (frecuencia mínima): "))
limite_superior = int(input("Ingrese límite superior (frecuencia máxima): "))
 
 
 
# Generación de la frecuencia aleatoria
frecuencia_objetivo = randint(limite_inferior, limite_superior)
 
 
 
# Ajuste si el número es múltiplo de 5
if frecuencia_objetivo % 5 == 0:
    if frecuencia_objetivo + 1 <= limite_superior:
        frecuencia_objetivo += 1
    else:
        frecuencia_objetivo -= 1
adivinado = False
 
 
 
# Primer intento
intento1 = int(input("Intento 1 - Ingrese la frecuencia a calibrar: "))
if intento1 == frecuencia_objetivo:
    print("Calibración exitosa.")
    adivinado = True
else:
    if frecuencia_objetivo > intento1:
        print("La frecuencia objetivo es mayor.")
    else:
        print("La frecuencia objetivo es menor.")
 
 
 
# Segundo intento
if not adivinado:
    intento2 = int(input("Intento 2 - Ingrese la frecuencia a calibrar: "))
    if intento2 == frecuencia_objetivo:
        print("Calibración exitosa.")
        adivinado = True
    else:
        if frecuencia_objetivo > intento2:
            print("La frecuencia objetivo es mayor.")
        else:
            print("La frecuencia objetivo es menor.")
        # Pista matemática utilizando valor absoluto
        distancia1 = abs(frecuencia_objetivo - intento1)
        distancia2 = abs(frecuencia_objetivo - intento2)
        print("Te daré una pista:")
        if distancia1 < distancia2:
            print(f"La frecuencia buscada está más cerca de {intento1} que de {intento2}.")
        elif distancia2 < distancia1:
            print(f"La frecuencia buscada está más cerca de {intento2} que de {intento1}.")
        else:
            print("Ambos intentos estuvieron a la misma distancia numérica.")
 
 
 
# Tercer intento
if not adivinado:
    intento3 = int(input("Intento 3 - Ingrese la última frecuencia a calibrar: "))