#Valores Bases
MA = 120000
SDA = 25000

edad = int(input("Ingrese su edad: "))
print("1.- Elite ")
print("2.- Pro ")
print("3.- Basico")
SP = input("Ingrese su opción: ")

if edad<=25:
    if SP == "1" or SP == "2":
        descuento_matricula = 0.20
    else:
        descuento_matricula = 0.10
elif 26<= edad <=50:
    if SP == "1" or "2":
        descuento_matricula = 0.15
    else:
        descuento_matricula = 0.05
else: 
    descuento_matricula = 0.0
PrecioMatriculaFinal = MA*(1-descuento_matricula)
print("El valor a pagar de la matricula es: $", PrecioMatriculaFinal)

              

