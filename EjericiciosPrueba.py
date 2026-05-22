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

cantjuegos = 0
Precio = 0
indies = 0
estudio = 0

while True:
    try:
        cantjuegos = int(input(("Cuantos juegos son?: ")))
        break
    except ValueError as er:
        print(er)

for i in range(cantjuegos):
    while True:
        Titulo = input("Ingrese el nombre del juego: ")
        if len(Titulo) < 5:
            print("Invalido: ingrese al menos un titulo con 5 caracteres")
            continue
        if ' ' in Titulo:
            print("Invalido: el titulo no debe contener espacios")
            continue
        if not Titulo.isupper():
            print("Invalido: el titulo debe estar en MAYÚSCULAS")
            continue
        break

    while True:
        try:
            Precio = int(input("Cual es el precio del juego: "))
            if Precio <= 0:
                print("Invalido: ingrese un número entero positivo")
                continue
            break
        except ValueError:
            print("Precio inválido: ingrese un número entero")

    if Precio > 20000 and Precio < 40000:
        indies = indies + 1
    elif Precio >= 40000:
        estudio = estudio + 1

print(f"Resumen: {indies} indies, {estudio} de estudio")

