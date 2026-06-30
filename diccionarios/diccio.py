autos = {

    "A001" : ["Toyota", "corolla", 2000, 5],
    "A002" : ["Ford", "Ranger", 2019,4],
    "A003" : ["Chevrolet", "Spark", 2022,4],
    "A004" : ["Suzuki", "Aerio", 2005,4],
    "A005" : ["Toyota", "Yaris", 20015,5]
}

operaciones = {

    "A001" : ["01-01-2024", "12-12-2025"],
    "A002" : ["07-08-2024", "01-08-2025"],
    "A003" : ["09-01-2025", "Pendiente"],
    "A004" : ["24-03-2025", "Pendiente"],
    "A005" : ["24-03-2024", "24-07-2024"]


}

def autos_vendidos_por_marca(marca):
    total = 0

    for id_auto, datos in autos.items():# ".items" para expulsar
        print(id_auto, datos)
        print(datos[0])

#main

autos_vendidos_por_marca("Toyota")