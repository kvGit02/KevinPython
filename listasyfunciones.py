#funciones
def suma(a,b):
    return a+b
def resta(a,b):
    return a-b

def multiplicacion(a,b):
    return a*b
def division(a,b):
    if b != 0:
        return a/b
    else:
        return "Error: División por cero no permitida"
def potencia(a,b):
    return a**b
def raiz(a):
    if a >= 0:
        return a**0.5
    else:
        return "Error: No se pueden calcular raíces de números negativos"
def factorial(n):
    if n < 0:
        return "Error: No se pueden calcular factoriales de números negativos"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def fibonacci(n):
    if n < 0:
        return "Error: No se pueden calcular números de Fibonacci para índices negativos"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
def mcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)
def mcm(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // mcd(a, b)
def es_par(n):
    return n % 2 == 0
def es_impar(n):
    return n % 2 != 0
def es_mayor(a, b):
    return a > b
def es_menor(a, b):
    return a < b
def es_igual(a, b):
    return a == b
def es_diferente(a, b):
    return a != b
def es_mayor_o_igual(a, b):
    return a >= b
def es_menor_o_igual(a, b):
    return a <= b
def es_divisible(a, b):
    if b != 0:
        return a % b == 0
    else:
        return "Error: División por cero no permitida"
def es_multiplo(a, b):
    if b != 0:
        return a % b == 0
    else:
        return "Error: División por cero no permitida"
def es_positivo(n):
    return n > 0
def es_negativo(n):
    return n < 0
def es_cero(n):
    return n == 0
def es_par_o_impar(n):
    if n % 2 == 0:
        return "par"
    else:
        return "impar"
def es_primo_o_compuesto(n):
    if n <= 1:
        return "no es primo ni compuesto"
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return "compuesto"
    return "primo"
def es_perfecto(n):
    if n < 1:
        return "Error: No se pueden calcular números perfectos para valores menores que 1"
    suma_divisores = sum(i for i in range(1, n) if n % i == 0)
    return suma_divisores == n
def es_abundante(n):
    if n < 1:
        return "Error: No se pueden calcular números abundantes para valores menores que 1"
    suma_divisores = sum(i for i in range(1, n) if n % i == 0)
    return suma_divisores > n
def es_deficiente(n):
    if n < 1:
        return "Error: No se pueden calcular números deficientes para valores menores que 1"
    suma_divisores = sum(i for i in range(1, n) if n % i == 0)
    return suma_divisores < n
def es_amigo(a, b):
    if a < 1 or b < 1:
        return "Error: No se pueden calcular números amigos para valores menores que 1"
    suma_divisores_a = sum(i for i in range(1, a) if a % i == 0)
    suma_divisores_b = sum(i for i in range(1, b) if b % i == 0)
    return suma_divisores_a == b and suma_divisores_b == a
def es_hermano(a, b):
    if a < 1 or b < 1:
        return "Error: No se pueden calcular números hermanos para valores menores que 1"
    suma_divisores_a = sum(i for i in range(1, a) if a % i == 0)
    suma_divisores_b = sum(i for i in range(1, b) if b % i == 0)
    return suma_divisores_a == suma_divisores_b
def es_cuadrado_perfecto(n):
    if n < 0:
        return "Error: No se pueden calcular cuadrados perfectos para números negativos"
    raiz = int(n**0.5)
    return raiz * raiz == n
def es_cubo_perfecto(n):
    if n < 0:
        return "Error: No se pueden calcular cubos perfectos para números negativos"
    raiz = int(n**(1/3))
    return raiz * raiz * raiz == n
def es_pentagonal(n):
    if n < 0:
        return "Error: No se pueden calcular números pentagonales para números negativos"
    k = (1 + (1 + 24 * n)**0.5) / 6
    return k.is_integer() and k > 0
def es_hexagonal(n):
    if n < 0:
        return "Error: No se pueden calcular números hexagonales para números negativos"
    k = (1 + (1 + 8 * n)**0.5) / 4
    return k.is_integer() and k > 0
#funciones de lista
def suma_lista(lista):
    return sum(lista)
def producto_lista(lista):
    result = 1
    for num in lista:
        result *= num
    return result
def promedio_lista(lista):
    if len(lista) == 0:
        return "Error: No se puede calcular el promedio de una lista vacía"
    return sum(lista) / len(lista)
def maximo_lista(lista):
    if len(lista) == 0:
        return "Error: No se puede calcular el máximo de una lista vacía"
    return max(lista)
def minimo_lista(lista):
    if len(lista) == 0:
        return "Error: No se puede calcular el mínimo de una lista vacía"
    return min(lista)
def mediana_lista(lista):
    if len(lista) == 0:
        return "Error: No se puede calcular la mediana de una lista vacía"
    sorted_lista = sorted(lista)
    n = len(sorted_lista)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lista[mid - 1] + sorted_lista[mid]) / 2
    else:
        return sorted_lista[mid]
def moda_lista(lista):
    if len(lista) == 0:
        return "Error: No se puede calcular la moda de una lista vacía"
    from collections import Counter
    count = Counter(lista)
    max_count = max(count.values())
    moda = [num for num, freq in count.items() if freq == max_count]
    return moda
def varianza_lista(lista):
    if len(lista) == 0:
        return "Error: No se puede calcular la varianza de una lista vacía"
    mean = promedio_lista(lista)
    return sum((x - mean) ** 2 for x in lista) / len(lista)
def desviacion_estandar_lista(lista):
    if len(lista) == 0:
        return "Error: No se puede calcular la desviación estándar de una lista vacía"
    return varianza_lista(lista) ** 0.5
def rango_lista(lista):
    if len(lista) == 0:
        return "Error: No se puede calcular el rango de una lista vacía"
    return max(lista) - min(lista)
def ordenamiento_lista(lista):
    return sorted(lista)
def invertir_lista(lista):
    return lista[::-1]
def eliminar_duplicados_lista(lista):
    return list(set(lista))
def contar_elementos_lista(lista):
    return len(lista)
def buscar_elemento_lista(lista, elemento):
    return elemento in lista
def indice_elemento_lista(lista, elemento):
    if elemento in lista:
        return lista.index(elemento)
    else:
        return "Error: Elemento no encontrado en la lista"
def concatenar_listas(lista1, lista2):
    return lista1 + lista2
def interseccion_listas(lista1, lista2):
    return list(set(lista1) & set(lista2))
def union_listas(lista1, lista2):
    return list(set(lista1) | set(lista2))
def diferencia_listas(lista1, lista2):
    return list(set(lista1) - set(lista2))
def diferencia_simetrica_listas(lista1, lista2):
    return list(set(lista1) ^ set(lista2))
def producto_cartesiano_listas(lista1, lista2):
    return [(a, b) for a in lista1 for b in lista2]
def subconjunto_lista(lista1, lista2):
    return set(lista1).issubset(set(lista2))
def superconjunto_lista(lista1, lista2):
    return set(lista1).issuperset(set(lista2))
#funciones de cadena
def longitud_cadena(cadena):
    return len(cadena)
def mayusculas_cadena(cadena):    return cadena.upper()
def minusculas_cadena(cadena):    return cadena.lower()
def capitalizar_cadena(cadena):    return cadena.capitalize()
def invertir_cadena(cadena):    return cadena[::-1]
def contar_caracteres_cadena(cadena, caracter):
    return cadena.count(caracter)
def buscar_subcadena_cadena(cadena, subcadena):    return cadena.find(subcadena)
def reemplazar_subcadena_cadena(cadena, subcadena_vieja, subcadena_nueva):
    return cadena.replace(subcadena_vieja, subcadena_nueva)
def es_palindromo_cadena(cadena):
    cleaned_cadena = ''.join(c for c in cadena if c.isalnum()).lower()
    return cleaned_cadena == cleaned_cadena[::-1]
def es_anagrama_cadena(cadena1, cadena2):
    cleaned_cadena1 = ''.join(c for c in cadena1 if c.isalnum()).lower()
    cleaned_cadena2 = ''.join(c for c in cadena2 if c.isalnum()).lower()
    return sorted(cleaned_cadena1) == sorted(cleaned_cadena2)
#mi lista de funciones es muy larga, si quieres que te explique alguna en particular, dime cual y con gusto te la explico.
#funcion con retorno y sin retorno
def funcion_con_retorno(a, b):
    return a + b
def funcion_sin_retorno(a, b):
    print(f"La suma de {a} y {b} es: {a + b}")
#funcion con parametros y sin parametros
def funcion_con_parametros(a, b):
    return a * b
def funcion_sin_parametros():
    return "Hola, mundo!"
