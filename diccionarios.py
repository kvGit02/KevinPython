# diccionario = {
#     "nombre": "Juan",
#     "edad": 30,
#     "ciudad": "Madrid"
# }
# print(diccionario["nombre"])  # Imprime: Juan
# print(diccionario["edad"])    # Imprime: 30
# print(diccionario["ciudad"])  # Imprime: Madrid

# # eliminar elemento del diccionario
# del diccionario["edad"]  # Elimina la clave "edad" y su valor asociado
# print(diccionario)  # Imprime: {'nombre': 'Juan', 'ciudad': 'Madrid'}
# añadir_elemento = {"profesion": "Ingeniero"}
# diccionario.update(añadir_elemento)  # Agrega el nuevo elemento al diccionario
# print(diccionario)  # Imprime: {'nombre': 'Juan', 'ciudad': 'Madrid', 'profesion': 'Ingeniero'}
# # y con el for?for clave, valor in diccionario.items():
# for clave, valor in diccionario.items():
#     print(f"{clave}: {valor}") 
# Imprime:
# nombre: Juan
# ciudad: Madrid    
# profesion: Ingeniero

# pokemon = {
#     "nombre": "Pikachu",
#     "tipo": "Eléctrico",
#     "nivel": 50,
#     "Hp": 1000,   
# }
# print("===Datos iniciales===")
# for key, value in pokemon.items():
#     print(key,":", value)

# pokemon["Habilidad"] = "Llamarada"
# print("\n=== Despues de insertar Habilidad" "===")
# for key, value in pokemon.items():
#     print(key, ":", value)

# pokemon["nivel"] = 200
# print("\n===Despues de actualizar 'nivel' ===")
# for key, value in pokemon.items():
#     print(key, ":", value)

# del pokemon["Hp"]
# print("\n=== Despues de borrar el dato 'Hp' ===")
# for key, value in pokemon.items():
#     print(key, ":", value)

#Tiempo

# Tiempo = {
#     "Dia":"Lunes",
#     "Clima":"Soleado",
#     "Temperatura":25,
#     "Humedad":58
# }

alumno = {
    "Nombre:":"Banana",
    "Edad:":25,
    "Carrera:":"Informatica",
    "Clave:":"Valor"
    }
def valores():
    clave = input("Ingrese la nueva clave: ").strip()
    valor = input("Ingresa el valor: ").strip()
    alumno[clave] = valor
    print(f"'{clave}' agregada correctamente.")

def borrar():
    clave = input("Que clave quieres borrar?: ")
    if clave in alumno:
        del alumno[clave]
        print(f"'{clave}' borrada correctamente.")
    else:
        print("Esa clave no existe")

def actualizar():
    clave = input("Que clave quieres actualizar?: ")
    if clave in alumno:
        valor = input("Nuevo valor: ").strip()
        alumno[clave] = valor
        print(f"'{clave}' actualizada correctamente.")
    else:
        print("Esa clave no existe")


def mostrar():
    print("\n=== Datos del alumno ===")
    for key, value in alumno.items():
        print(f"{key}: {value}")


while True:
    print("\n ===Menu===")
    print("1.- Agregar dato")
    print("2.- Borrar dato")
    print("3.- Actualizar dato")
    print("4.- Mostrar dato")
    print("5.- Salir")

    opcion = input("Elige una opcion: ").strip()

    match opcion:
        case "1":
            valores()
            print("Dato agregado correctamente.")
        case "2":
            borrar()
            print("Dato borrado correctamente.")
        case "3":
            actualizar()
            print("Dato actualizado correctamente.")
        case "4":
            mostrar()
        case "5":
            print("Saliendo")
            break
        case _:
            print("Opcion invalida, intente denuevo")