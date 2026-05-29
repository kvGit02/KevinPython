print("¡Bienvenido al sistema de gestión de préstamos de la Biblioteca Central!")
libros=120
opcion=0
prestamo2=0
while opcion!=5:
    print("===MENÚ PRINCIPAL===")
    print("1. Libros disponibles")
    print("2. Realizar préstamo")
    print("3. Devolver préstamo")
    print("4. Historial de préstamos")
    print("5. Salir")
    opcion=int(input("ingrese la opcione querida: "))
    if opcion==1:
        print(f"Esta es la cantidad de libros actual {libros}")
    elif opcion==2:
        prestamo=int(input("Cuantos libros quiere que le prestemos? "))
        if prestamo<=0 or prestamo>libros:
            print("Por favor ingrese una cantidad coeherente de libros")
        else:
            libros=libros-prestamo
            prestamo2=prestamo2+1
    elif opcion==3:
        devolver=int(input("Cuantos libros quiere devolver? "))
        devolver2=libros+devolver
        if devolver>0:
            libros=libros+devolver
            prestamo2=prestamo2-1
        elif devolver2<120:
            libros=libros+devolver
            prestamo2=prestamo2-1
        else:
            print("No puede superar el limite de la biblioteca (120 libros)")
    elif opcion==4:
        print(f"Esta es la cantidad de prestamos activos que tiene {prestamo2}")
print("Gracias por utilizar nuestro software, hasta la próxima.")



especialista=0
residente=0
while True:
    try:
        medicos=int(input("Cuantos medicos desea ingresar? "))
        break
    except:
        print("¡Registro médico inválido! Ingresa un entero positivo para continuar.")
for i in range(medicos):
    nombre=input("Ingrese su nombre (Debe tener al menos 6 caracteres y sin espacios) ")
    try:
        experiencia=int(input("Cuantos años de experiencia tiene? "))
    except:
        print("¡Error clínico! Ingresa un número entero positivo para la experiencia.")
        break
    if experiencia<=5:
        residente=residente+1
    elif experiencia>5:
        especialista=especialista+1
print(f"¡El hospital cuenta con {especialista} Especialistas Senior y {residente} Residentes Junior! ¡Sistema listo para operar!")