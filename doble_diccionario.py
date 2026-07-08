#Funciones guia examen
 
 
 
autos = {
    'A001' : ['Toyota','Corolla',2010,5],
    'A002' : ['Ford', 'Ranger',2019,4],
    'A003' : ['Chevrolet', 'Spark',2022,4],
    'A004' : ['Suzuki', 'Aerio',2005,4],
    'A005' : ['Toyota','Yaris',2015,5],
    'A006' : ['Chevrolet', 'Impala',1950,1],
}
operaciones = {
    'A001' : ['01-01-2024','12-12-2025'],
    'A002' : ['07-08-2024','Pendiente'],
    'A003' : ['09-01-2025','Pendiente'],
    'A004' : ['24-03-2025','Pendiente'],
    'A005' : ['24-03-2024','24-07-2024'],
    'A006' : ['24-03-2024','24-09-2024'],
}
 
#Muestra todos los vehiculos
def muestraAutos(dic):
    for id, vehiculo in dic.items():
        print(f"{id}.- {vehiculo}")
    print("-"*50)

# ejercicio 1
 
def autos_vendidos_por_marca(marca):
    total = 0
    for id_auto, datos in autos.items():
        if datos[0].lower() == marca.lower():
            if operaciones[id_auto][1] != 'Pendiente':
                total += 1
    print(f'El número total de autos vendidos de la marca {marca.upper()} es {total}')
 
# Busqueda por año
#Ejercicio 2 

def busqueda_por_anio(anio_min, anio_max):
    elementos_encontrados = []
 
 
    for id_auto, datos in autos.items():
        marca = datos[0]
        modelo = datos[1]
        anio = datos[2]
 
 
        if anio_min <= anio <= anio_max:
            if operaciones[id_auto][1] == 'Pendiente':
                elementos_encontrados.append(f'{marca} {modelo} -- {id_auto}')
    
    if elementos_encontrados:
        elementos_encontrados.sort()
        print(elementos_encontrados)
    else:
        print('No se han encontrado elementos')
 
 
 
 
## MAIN
 
 
#test autos_vendidos_por_marca
#marca = input('Ingrese la marca a buscar: ')
#autos_vendidos_por_marca(marca)
 
 
#test busqueda_por_anio
 
 
# while True:
#     try: 
#         anio_inicio = int(input('Ingrese en año de inicio de la búsqueda: '))
#         anio_termino = int(input('Ingrese en año de término de la búsqueda: '))
#         busqueda_por_anio(anio_inicio,anio_termino)
#         break
#     except:
#         print('Los años ingresados deben ser número enteros')

#Ejercicio 3
def actualizar_fecha_venta(id_auto, nueva_fecha):
    if id_auto in autos:
        operaciones[id_auto][-1]=nueva_fecha
        return True
    else:
        
        return False

# while True:
#     id=input("Ingrese el valor del ID a Actualizar: ")
#     fecha=input("Ingrese la fecha a Actualizar: ")

#     if actualizar_fecha_venta(id, fecha):
#         print("Actualizado correctamente")
#     else:
#         print("El id no se encuenta")
#     next=input("¿Desea actualizar otro vehículo (s/n)?")
#     if next.lower()=="n":
#         break

# Ejercicio 4

def validaAnio(a):
    if a<1900:
        return True
    else:
        return False
def validaRanking(a):
    if a<1 or a>5:
        return True
    else:
        return False

def validString(s):
    if s==""  or s==" ":
        return True
    else:
        return False

print(validString("Algo"))


def creAuto():
    id=input("Ingrese el ID: ")
    if validString(id):
        print("Dato incorrecto")
        return
    marca=input("Ingrese la marca: ")
    if validString(marca):
        print("Dato incorrecto")
        return
    modelo=input("Ingrese el modelo: ")
    if validString(modelo):
        print("Dato incorrecto")
        return
    anio=int(input("Ingrese el año: "))
    if validaAnio(anio):
        print("El año debe ser superior a 1900")
        return
    ranking=int(input("Ingrese el ranking: "))
    if validaRanking(ranking):
        print("El ranking debe estar entre 1 y 5")
        return
    fecha=input("Ingrese la fecha: ")
    if validString(fecha):
        print("Dato incorrecto")
        return

    autos[id]=[marca,modelo,anio,ranking]
    operaciones[id]=[fecha,'Pendiente']

# muestraAutos(autos)
# creAuto()
# muestraAutos(autos)


# Ejercicio 5
def eliminar_auto(id_auto):
    if id_auto in autos:
        del autos[id_auto]
        del operaciones[id_auto]
        return True
    else:
        
        return False

def actFecha():
    while True:
        id=input("Ingrese el valor del ID a Actualizar: ")
        fecha=input("Ingrese la fecha a Actualizar: ")

        if actualizar_fecha_venta(id, fecha):
            print("Actualizado correctamente")
        else:
            print("El id no se encuenta")
        next=input("¿Desea actualizar otro vehículo (s/n)?")
        if next.lower()=="n":
            break

def buscaXAnio():
    while True:
        try: 
            anio_inicio = int(input('Ingrese en año de inicio de la búsqueda: '))
            anio_termino = int(input('Ingrese en año de término de la búsqueda: '))
            busqueda_por_anio(anio_inicio,anio_termino)
            break
        except:
            print('Los años ingresados deben ser número enteros')

# Menu princial 

def mainMenu():
    while True:
        try:
            print("====Opciones====")
            print("1.- Ingreasar Auto")
            print("2.- Eliminar Auto")
            print("3.- Actualizar, fecha venta")
            print("4.- Ingreasar Auto")
            print("5.- Ingreasar Auto")
            print("9.- Salir")
            op=int(input("Seleccione una opcion: "))
            match op:
                case 1:
                    creAuto()
                case 2:
                    id=input("Ingrese el ID a eliminar: ")
                    eliminar_auto(id)
                case 3:
                    actFecha()
                case 4:
                    buscaXAnio()
                case 5:
                    marca=input("Ingrese la marca a revisar: ")
                    autos_vendidos_por_marca(marca)
                case 9:
                    print("Salir")
                    break
                case _:
                    print("Opcion invalida")  
        except Exception as e:
            print("Error :", e)
