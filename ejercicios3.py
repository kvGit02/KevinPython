# El programa debe tener un menú de opciones de donde se pueda realizar el pago del cupo de la tarjeta de crédito, como también simular nuevas compras, y estas una vez sumadas se resten al cupo disponible. 
# Las opciones disponibles deben estar construidas de la siguiente forma:
# 1.	Pago de Tarjeta de Crédito:
# a.	El usuario comienza con una deuda de $100.000
# b.	El usuario puede ingresar un monto para realizar un pago en la tarje-ta de crédito.
# c.	Se debe verificar que el monto ingresado sea mayor o igual a cero.
# d.	Se debe verificar que el monto a pagar no exceda la deuda actual de la tarjeta.
# e.	Al pagar el sistema debe descontar de la deuda total
# f.	Si las verificaciones son exitosas, se realiza el pago y se actualiza el saldo de la tarjeta.
# 2.	Simulación de Compras:
# a.	El usuario puede simular realizar un número ilimitado de compras.
# b.	Para cada compra, se solicita al usuario ingresar el monto de la compra. El programa suma los montos de cada compra. 
# c.	Se verifica que el monto de la compra sea mayor o igual a cero.
# d.	Se realiza la compra y se actualiza el saldo de la tarjeta para cada iteración del bucle for.
# 3.	Salir:
# a.	Al seleccionar esta opción, el programa debe cerrarse o finalizar.

# A considerar:
# 1.	Manejo de Errores:
# a.	Se utilizan bloques try y except para manejar posibles errores al in-gresar datos, validar valores no numéricos y errores inesperados. 
# b.	Se debe programar mensajes de error específicos para guiar al usuario sobre posibles problemas.
Deuda = 100000
op = 0
while op !=4:
    try:
        print("1.- Pagar con tarjeta de credito \n 2.- Comprar \n 3.- Cupo disponible \n 4.- Salir")
        op = int(input("Elija una opcion(1-4):"))

        if op == 1:
            print("1.- Realizar el pago con la tarjeta")
            print("2.- Salir")
            subop1 = int(input("Elija una opcion(1-2): "))
            while subop1 !=2:
                try:
                    if subop1 == 1:
                        print("Cuanto desea agregar a la tarjeta")
                        


    except ValueError:
        print("Debe de ser un numero mayor a 0!!!!!!!!!!!!")