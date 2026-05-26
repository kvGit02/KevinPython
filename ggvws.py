print("Umbral")
print("--------------------------------")

nivel_numerico = 0
contador_pais_desarrollado = 0
contador_pais_no_desarrollado = 0


nivel_numerico = int(input("Ingrese el nivel numerico del pais:"))


if nivel_numerico <= 40:
    print("Pais en vias de desarrollo")
    contador_pais_no_desarrollado +=1
    #contador_pais_no_desarrollado
else:
    print("Pais desarrollado")
    contador_pais_desarrollado +=1
    #contador_pais_desarrollado

print("Reporte")
print("-------")
print(f"Paises desarrollados {contador_pais_no_desarrollado}")
print(f"Paises desarrollados {contador_pais_desarrollado}")
