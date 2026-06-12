# ### Tiempo
# tiempo = { 
#     "Dia":"Lunes",
#     "Clima":"Nublado",
#     "Temperatura":"25",
#     "Humedad":"60%"
# }
# ##funcion
# import time

# def muestra():
#     for key, value in tiempo.items():
#         print(key, value)

# def añadir():
#     keyadd=input("Ingrese la categoria deseada: ")
#     valueadd=input("Ingrese dato de la categoria: ")
#     tiempo[keyadd]=valueadd


# while True:
#     try:
#         print("¿Que desea hacer?")
#         print('''
#             1.-Añadir datos
#             2.-Elimiar datos
#             3.-Actualizar datos
#             4.-Mostrar datos
#             5.-chao
#             ''')
#         opc=int(input("Ingrese opcion -> "))
#         match opc:
#             case 1:
#                 añadir()
#                 print("Dato añadido!")
#                 time.sleep(1)
#             case 2:
#                 print("")
#             case 3:
#                 print("")
#             case 4:
#                 muestra()
#                 time.sleep(3)
#             case 5:
#                 print("Cerrando programa...")
#                 time.sleep(2)
#                 break
#     except ValueError:
#         print("Ocurrió un error. Por favor, inténtelo de nuevo.")




Juegos={
  "Hackandslash":"Devil may cry 3 ",
  "run and gun": "Cuphead" ,
  "Plataformer" : "Super mario galaxy" ,
  "Rpg": "Final fantasy 7"
}
def agregar():
  key = input("Clave a agregar: ").strip()
  value = input("Valor: ").strip()
  Juegos[key] = value
  print(f"'{key}' agregado.")

def borrar():
  eliminar = input("Que desea eliminar? ").strip()
  if eliminar in Juegos:
    del Juegos[eliminar]
    print(f"'{eliminar}' eliminado.")
  else:
    print("La clave no existe.")

def actualizar():
  Juegos["Rpg"] = "Final Fantasy Remake Integrade"
  print("Rpg actualizado.")

def mostrar():
  for k, v in Juegos.items():
    print(f"{k}: {v}")

while True:
  print("\n1.- Agregar dato")
  print("2.- Borrar datos")
  print("3.- Actualizar")
  print("4.- Mostrar datos")
  print("5.- Salir")

  try:
    op = int(input("Elija una opcion -> ").strip())
  except ValueError:
    print("Opción inválida. Ingrese un número.")
    continue

  if op == 1:
    agregar()
  elif op == 2:
    borrar()
  elif op == 3:
    actualizar()
  elif op == 4:
    mostrar()
  elif op == 5:
    break
  else:
    print("Opción inválida.")
