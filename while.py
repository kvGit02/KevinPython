## Ecplicacion y ejemplos de while

## tabla de multiplicar con while
cont=1
num=8
while cont<=10:
    print(f"{num}x{cont}={num*cont}")
    cont+=1


## codigo secreto
code=3434

pwd=int(input("Ingrese el pin: "))

while code!=pwd:
    print("Error , intente de vuelta") 
    pwd=int(input("Ingrese el pin: "))
print("Acceso correcto")
