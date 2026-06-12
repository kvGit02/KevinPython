### Tiempo
tiempo = { 
    "Dia":"Lunes",
    "Clima":"Nublado",
    "Temperatura":"25",
    "Humedad":"60%"
}
##funcion
import time

def muestra():
    for key, value in tiempo.items():
        print(key, value)

def añadir():
    keyadd=input("Ingrese la categoria deseada: ")
    valueadd=input("Ingrese dato de la categoria: ")
    tiempo[keyadd]=valueadd


while True:
    try:
        print("¿Que desea hacer?")
        print('''
            1.-Añadir datos
            2.-Elimiar datos
            3.-Actualizar datos
            4.-Mostrar datos
            5.-chao
            ''')
        opc=int(input("Ingrese opcion -> "))
        match opc:
            case 1:
                añadir()
                print("Dato añadido!")
                time.sleep(1)
            case 2:
                print("")
            case 3:
                print("")
            case 4:
                muestra()
                time.sleep(3)
            case 5:
                print("Cerrando programa...")
                time.sleep(2)
                break
    except ValueError:
        print("Ocurrió un error. Por favor, inténtelo de nuevo.")