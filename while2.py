## Ejemplo y uso de while
# cont=1
# while cont<=3:
#     print(f"Contador {cont}")
#     cont+=1

# pin=3535

# code=int(input("Ingrese su pin: "))

# while pin!=code:
#     print("Error, intente de nuevo")
#     code=int(input("Ingrese su pin: "))
# print("PIN CORECTO!")


# ## usando whiel, pida al usuario un nuemro 
# # y muestre su tabla de multiplicar hasta el 10.

# num=int(input("Ingrese un numero"))
# c=1
# while c<=10:
#     print(f"{num}x{c}={c*num}")
#     c+=1


# Votatoon

toon1=input("Ingrese el toon 1: ")
toon2=input("Ingrese el toon 2: ")

v1=0
v2=0
cant=int(input("Cauntos votantes son? "))
while cant>0:
    # pedir votos
    voto=int(input(f"Por quien votará? 1.- {toon1} 2.- {toon2}: "))
    if voto==1:
        v1+=1
    elif voto==2:
        v2+=1
    else:
        print("Voto nulo")
    cant-=1

if v1>v2:
    print(f"Gano {toon1} con {v1} votos")
elif v2>v1:
    print(f"Gano {toon2} con {v2} votos")
else:
    print("Fue un empate")

