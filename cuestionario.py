print("---Cuestionario---")
print("Cual de los siguientes animales vive en el agua?:")
print("a.- Perro")
print("b.- Cocodrillo")
print("c.- Conejo")
print("d.- Tiburon")
puntaje=0
res=input()
if res=="b":
    puntaje=0.5
elif res=="d":
    puntaje=1.5
else:
    print("Respuesta Incorrecta!")
print("Tu puntaje es:",puntaje)