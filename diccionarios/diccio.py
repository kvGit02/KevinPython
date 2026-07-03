autos = {
                #0       #1        #2
    "A001" : ["Toyota", "corolla", 2010, 5],
    "A002" : ["Ford", "Ranger", 2019,4],
    "A003" : ["Chevrolet", "Spark", 2022,4],
    "A004" : ["Suzuki", "Aerio", 2005,4],
    "A005" : ["Toyota", "Yaris", 20015,5],
    "A006" : ["Chevrolet", "Impala", 1950,1]
}
#autos que no se venden estan "Pendiente"
operaciones = {
   #id_auto       #0              #1
    "A001" : ["01-01-2024", "12-12-2025"],
    "A002" : ["07-08-2024", "Pendiente"],
    "A003" : ["09-01-2025", "Pendiente"],
    "A004" : ["24-03-2025", "Pendiente"],
    "A005" : ["24-03-2024", "24-07-2024"],
    "A006" : ["24-03-2024", "24-09-2024"]
                  #0              #1

}

def muestraAutos(dic):
    for id, vehiculo in dic.items():
        print(f"{id}.- {vehiculo}")
        



def autos_vendidos_por_marca(marca):
    total = 0

    for id_auto, datos in autos.items():# ".items" para expulsar
        # print(id_auto, datos)
        # print(datos[0])
        if datos[0].lower() == marca.lower():
            if operaciones[id_auto][1] != "Pendiente":
                total +=1
        
    print(f"El numero total de autos vendidos de la marca {marca.upper()} es {total}")

#main
# marca = input("Ingrese la marca a buscar: ")
# autos_vendidos_por_marca(marca)

def busqueda_por_añio(añio_min, añio_max):
    elementos_encontrados = []
    for id_auto, datos in autos.items():
        marca = datos[0]
        modelo = datos[1]
        añio = datos[2]

        if añio_min <= añio <= añio_max:
            if operaciones[id_auto][1] == "Pendiente":
                elementos_encontrados.append(f"{marca} {modelo} -- {id_auto}")

    if elementos_encontrados:
        elementos_encontrados.sort()
    else:
        print("No se han encontrado elementos")

    print(id_auto)
#test_busqueda_por_año
# while True:
#     try:
#         añio_inicio = int(input("Ingrese el año de inicio de la busqueda: "))
#         añio_termino = int(input("Ingrese el año de termino de la busqueda: "))
#         busqueda_por_añio(añio_inicio,añio_termino)
#         break
#     except:
#         print("Los años ingresados deben ser numeros enteros")


busqueda_por_añio(2005, 2025)
#Ejercicio 3:
def actualizar_fecha_venta(id_auto, nueva_fecha):
    if id_auto in autos:
        operaciones[id_auto][-1]=nueva_fecha
    else:
        print("El id no se encuentra")
        return False
    
while True:
    id = input("Ingrese el valor del ID a actualizar")
    fecha = input("Ingrese la fecha a actualizar")

    if actualizar_fecha_venta(id, fecha):
        print("Actualizado correctamente")
    else:
        print("El id no se encuentra")
    next = input("Desea actualizar otro vehiculo (s/n)?")
    if next.lower() == "n":
        break
#Ejercicio 4:

def validaAÑio(a):
    if a < 1900:
        return True
    else:
        return False
    
def validaRanking(a):
    if a <=1 and a > 5:
        return True
    else:
        return False
    
def validString(s):
    if "s" =="" or s ==" ":
        return True
    else:
        return False
validString("Algo")

print(validaRanking(0))
def creaAuto():
    id = input("Ingrese el ID:")
    if validString(id):
        print("Dato incorrecto")
        return
    marca = input("Ingrese la marca:")
    if validString(marca):
        print("Dato incorrecto")
        return
    modelo = input("Ingrese el modelo:")
    if validString(modelo):
        print("Dato incorrecto")
        return
    añio = input("Ingrese el añio:")
    if validaAÑio(añio):
        print("El añio debe ser superior a 1900")
        return
    ranking = input("Ingrese el ranking:")
    if validaRanking(ranking):
        print("El ranking tiene que ser un numero entero entre 1 y 5")
    fecha = input("Ingrese la fecha:")
    autos[id] = [marca, modelo, añio, ranking]
    operaciones[id] = [fecha, "Pendiente"]



muestraAutos(autos)
creaAuto()
muestraAutos(autos)

def eliminar_auto(id_auto):
    if id_auto in autos:
        del autos[id_auto]
        del operaciones[id_auto]
        return True
    else:
        return False
    
#Menu principal

print("===MENU PRINCIPAL===")
print("1.- Registrar nuevo auto")
print("2.- ")
print("3.- ")
print("4.- ")
print("5.- Eliminar auto")
print("6.- ")