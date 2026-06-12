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

pokemon = {
    "nombre": "Pikachu",
    "tipo": "Eléctrico",
    "nivel": 50,
    "Hp": 100,   
}
print("===Datos iniciales===")
for key, value in pokemon.items():
    print(key,":", value)

pokemon["Habilidad"] = "Llamarada"
print("\n=== Despues de insertar Habilidad" "===")
for key, value in pokemon.items():
    print(key, ":", value)

pokemon["nivel"] = 75
print("\n===Despues de actualizar 'nivel' ===")
for key, value in pokemon.items():
    print(key, ":", value)

del pokemon["Hp"]
print("\n=== Despues de borrar el dato 'Hp' ===")
for key, value in pokemon.items():
    print(key, ":", value)