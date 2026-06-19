## Crear un gestor de pacientes

pacientes=[
    {"nombre": " Aquiles Baeza", "prevision": "Fonasa", 
     "temperatura":39.6, "grave": True}, # 0
    {"nombre": " dON rAMON Baeza", "prevision": "Fodesa", 
     "temperatura":34.6, "grave": False},# 1
    {"nombre": " Señor Barriga ", "prevision": "Fonasa", 
     "temperatura":35.6, "grave": False}# 2
]

listadeNombres=[]
for ln in pacientes:
    listadeNombres.append(ln["nombre"])
print(listadeNombres)
# validad el estado de todos los pacientes ingresados

def quitarPaciente():
    eli = input("Ingrese el nombre o número del paciente que quiere quitar: ").strip()
    # intentar interpretar como índice
    try:
        idx = int(eli) - 1
        if 0 <= idx < len(pacientes):
            removed = pacientes.pop(idx)
            print(f"Paciente removido: {removed['nombre']}")
        else:
            print("Índice fuera de rango")
    except ValueError:
        # buscar por nombre
        found = False
        for i, p in enumerate(pacientes):
            if p["nombre"].strip().lower() == eli.lower():
                removed = pacientes.pop(i)
                print(f"Paciente removido: {removed['nombre']}")
                found = True
                break
        if not found:
            print("Paciente no encontrado")

# crear al gestor de pacientes en un centro medico
# Para poner el nombre se debe validar que no este vacio 
# y ademas tenga mas de 8 caracteres
# Para la prevision de salud solo exiten 3 posibles valores
# Fonasa, Isapre, o Fodesa
# Al ingresar un paciente, se debe poner la temperatura
# Crear una funcion que valide si esta grave o no
# Para que este grave debe tener mas de 39°
# Cada atencion vale $25.000
# Los despcuentos corresponden a 
# FOnasa 54%
# Isapre 27%
# Fodesa 12,5%
def MenuPacientes():
    while True:
        try:
            print("1.- Ingresar Paciente")
            print("2.- Quitar Paciente")
            print("3.- Tomar Temperatura")
            print("4.- Cobra Atencion")
            print("5.- Mostrar Pacientes")
            print("9.- Salir")
            op = int(input("Seleccione una opcion: "))
            match op:
                case 1:
                    nombre = input("Ingrese el nombre del paciente: ").strip()
                    if len(nombre) < 8:
                        print("El nombre debe tener al menos 8 caracteres")
                        continue
                    prevision = input("Ingrese la prevision de salud (Fonasa, Isapre, Fodesa): ").strip().title()
                    if prevision not in ["Fonasa", "Isapre", "Fodesa"]:
                        print("La prevision de salud debe ser Fonasa, Isapre o Fodesa")
                        continue
                    temperatura = float(input("Ingrese la temperatura del paciente: "))
                    grave = temperatura > 39
                    pacientes.append({"nombre": nombre, "prevision": prevision, "temperatura": temperatura, "grave": grave})
                case 2:
                    eli = input("Ingrese el nombre o número del paciente que quiere quitar: ").strip()
                    # intentar interpretar como índice
                    try:
                        idx = int(eli) - 1
                        if 0 <= idx < len(pacientes):
                            removed = pacientes.pop(idx)
                            print(f"Paciente removido: {removed['nombre']}")
                        else:
                            print("Índice fuera de rango")
                    except ValueError:
                        # buscar por nombre
                        found = False
                        for i, p in enumerate(pacientes):
                            if p["nombre"].strip().lower() == eli.lower():
                                removed = pacientes.pop(i)
                                print(f"Paciente removido: {removed['nombre']}")
                                found = True
                                break
                        if not found:
                            print("Paciente no encontrado")
                case 3:
                    for p in pacientes:
                        print(f"{p['nombre']}: {p.get('temperatura', 'N/A')}°C - {'Grave' if p.get('grave') else 'No grave'}")
                case 4:
                    base = 25000
                    for p in pacientes:
                        pre = p.get('prevision', '').lower()
                        if pre == 'fonasa':
                            disc = 0.54
                        elif pre == 'isapre':
                            disc = 0.27
                        else:
                            disc = 0.125
                        total = base * (1 - disc)
                        print(f"{p['nombre']}: ${total:,.0f}")
                case 5:
                    if len(pacientes) == 0:
                        print("No hay pacientes")
                    else:
                        c = 1
                        for p in pacientes:
                            print(f"{c} .- {p}")
                            c += 1
                        print("-" * 50)
                case 9:
                    print("Saliendo")
                    break
        except ValueError as e:
            print("Entrada inválida:", e)

