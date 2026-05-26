# Se debe construir un fragmento de
# código que solicite al usuario la cantidad de registros que desea procesar. El
# programa debe iterar indefinidamente hasta que se ingrese un número entero
# positivo. Ante cualquier entrada no válida (letras, símbolos o números negativos),
# se debe capturar la excepción y emitir el mensaje: “¡Número inválido! Ingresa un
# entero positivo para continuar el entrenamiento.
# numeros_registros = 0

# print("Sistema Registros")
# print("-----------------")
# while True:
#     try:
#         numeros_registros = int(input("Cuantos registros desea procesar?:"))


#         if numeros_registros > 0:
#             print(f"El numero de registros a procesar es {numeros_registros}")
#             break
#         else:
#             print("El numero ingresado deber ser positivo y mayor a 0")

#     except ValueError:
#         print("¡Número inválido! Ingresa un entero positivo para continuar el registro.")

# print(numeros_registros)

# Se requiere codificar una
# validación para un nombre de registro (ej. Nombre Ciudad). El programa debe
# verificar que la cadena ingresada posea una longitud mínima de 6 caracteres y no
# contenga ningún espacio en blanco.

print("Sistema de registro")
print("-------------------")
while True: 
    nombre_registro = input("Ingrese el nombre de la ciudad: ")
    largo_cadena = len(nombre_registro)

    if largo_cadena >=6:
        if " " not in nombre_registro:
            print("Nombre de regsitro correcto")
        else:
            print("El nombre no debe contener espacios")
    else:
        print("El largo del nombre de registro debe de ser de 6 caracteres y sin espacios")

