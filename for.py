#explicación y uso de For
#El i comienza en cero
#cantidad de repeticiones# --> 5(max)
# for i in range(1,6): #aca se omite el 0
#     print(i)
#empieza desde el 0 porque es el indice de la lista, y termina en el 4 porque el 5 no se incluye
# for i in range(5): #empieza desde el 0 y termina en el 4
#     print(i+1) #imprime el numero de iteracion, sumando 1 para que empiece desde el 1 en lugar del 0



# pedir un numero al usuario y mostrar su tabla de multiplicar
num=int(input("Ingrese el numero que desea multiplicar: "))
for i in range(1,num+1):
    print(f"{num} x {i} = {num*i}")

# Pedir al usuario la cantidad de notas 
# Mostrar el promedio de las notas ingresadas
# 4notas
notas = int(input("Ingrese la cantidad de notas: "))
suma=0
for i in range(notas):
    n=float(input(f"Ingrese la nota {i+1}: "))
    suma=suma+n
prom=suma/notas
print("El promedio es", round(prom,1))

if prom>=4:
    print("Alumno aprobado")
else:
    print("Alumno Reprovado")
#sumatoria
num=int(input("Ingrese la cantidad de notas: "))
total=0
for i in range(1, num+1):
    total+=i+1
print(f"El resultado total es {total}")
#factorial

