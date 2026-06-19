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



def validarEstados(pacientesHospital):
    for p in pacientesHospital:
        p["grave"]=validarEstado(p["temperatura"])


listado=[4,6,{"pokemon":"Eevee"},67,6]
#        0 1    2                3  4
print(listado[2]["pokemon"])

print(pacientes[1]["nombre"])
'''crear al gestor de pacientes en un centro medico
Para poner el nombre se debe validar que no este vacio 
y ademas tenga mas de 8 caracteres
Para la prevision de salud solo exiten 3 posibles valores
Fonasa, Isapre, o Fodesa
Al ingresar un paciente, se debe poner la temperatura
Crear una funcion que valide si esta grave o no
Para que este grave debe tener mas de 39°
Cada atencion vale $25.000
Los despcuentos corresponden a 
FOnasa 54%
Isapre 27%
Fodesa 12,5%

'''

pacientes.append({"nombre": "Alan Brito", "prevision": "Isapre", 
     "temperatura":39.6, "grave": True})



def validarEstado(tempe):
   if tempe>39:
       return True 
   else:
       return False
def mostrarPacientes():
    if len(pacientes)==0:
        print("No hay pacientes")
    else:
        c=1
        for p in pacientes:
            print(f"{c} .- {p}")
            c+=1
def agregarPaciente():
    nombre=input("Ingrese nombre: ")
    prevision=input("Ingrese prevision: ")
    temp=float(input("Ingrese temp: "))
    pacientes.append({"nombre": nombre, "prevision": prevision, 
                "temperatura":temp, "grave": validarEstado(temp)})
    print("Paciente agregado al listado")
def eliminarPaciente():
    mostrarPacientes()
    paci=int(input("Que paciente se vá?: "))
    pacientes.pop(paci-1)
    print("Paciente eliminado.")
def tomarTemp():
    mostrarPacientes()
    paciente=int(input("Qué paciente le tomará la temperatura?: "))
    temperatura=float(input("Ingrese la temperatura del paciente: "))
    pacientes[paciente-1]["temperatura"]=temperatura
    pacientes[paciente-1]["grave"]=validarEstado(temperatura)
    print("Temperatura y estado actualizado")
def cobrarAtencion():
    total=0
    mostrarPacientes()
    cobrar = int(input("¿A que paciente le va a cobrar?: "))
    prevision = pacientes[cobrar-1]["prevision"]

    if prevision.lower() == "fonasa":
        total = 25000 * 0.46
    if prevision.lower() == "isapre":
        total = 25000 * 0.73
    if prevision.lower() == "fodesa":
        total = 25000 * 0.875
    else:
        print("Prevision invalida")
    print(f"El total a pagar es: {total}")
    

def menuPacientes():
    while True:
        try:
            print("1.- Ingresar paciente")
            print("2.- Quitar paciente")
            print("3.- Tomar Temperatura")
            print("4.- Cobra atencion")
            print("5.- Mostrar Pacientes")
            print("9.- Salir")
            op=int(input("Ingrese una opcion: "))
            match op:
                case 1:
                    agregarPaciente()
                case 2:
                    eliminarPaciente()
                case 3:
                    tomarTemp()
                case 4:
                    cobrarAtencion()
                case 5:
                    mostrarPacientes()
                case 9:
                    print("Saliendo")
                    break
                case _:
                    print("Opción inválida")
        except Exception as e:
            print("Error:" , e)

# menuPacientes()

mostrarPacientes()

pacientes[1]["temperatura"]=39.6
pacientes[3]["temperatura"]=36.4
input("Cambios de temperatura")
validarEstados(pacientes)
input("Actualizacion de estado de cada paciente")
mostrarPacientes()