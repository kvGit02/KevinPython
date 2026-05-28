# Se debe estructurar un ciclo while que
# despliegue un menú principal con 5 opciones operativas. El programa debe
# mantenerse en ejecución continua hasta que se seleccione explícitamente la
# opción número 5. Al confirmar la salida, se debe emitir el mensaje: "Gracias por
# utilizar nuestro software, hasta la próxima".


while True:
        op = int(input("Seleccione una opcion(1-5): "))
        print("1.- Lol")
        print("2.- Lol")
        print("3.- Lol")
        print("4.- Lol")
        print("5.- Salir")

        if op == 1:
            print("Ejecutando la primera opcion")
        elif op == 2:
            print("Ejecutando la segunda opcion")
        elif op == 3:
                print("Ejecutando la tercera opcion")
        elif op == 4:
                print("Ejecutando la cuarta opcion")
        elif op == 5:
                print("Gracias por utilizar nuestro software, hasta la proxima")
                pass
        else:
            print("Opcion invalida, Intente denuevo")