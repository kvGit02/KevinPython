aprobados = 0
reprobados = 0

while True:
    try:
        n = int(input("Cuantos estudiantes son?: "))
        break
    except ValueError:
        print("Solo numeros enteros")

for i in range(n):              # ✅ fuera del while True
    print(f"Estudiante numero: {i+1}")

    while True:                 # ✅ dentro del for i
        nombre = input("Nombre: ").strip()
        if len(nombre) >= 3:
            break
        print("Minimo 3 letras.")

    total_notas = 0             # ✅ dentro del for i
    for j in range(3):          # ✅ dentro del for i
        while True:
            try:
                nota = float(input(f"Nota {j+1} (1.0 - 7.0): "))
                if 1.0 <= nota <= 7.0:
                    total_notas += nota
                    break
                print("La nota debe estar entre 1.0 y 7.0")
            except ValueError:
                print("Solo numeros")

    promedio = total_notas / 3  # ✅ fuera del for j, dentro del for i
    print(f"Promedio de {nombre}: {promedio:.1f}")

    if promedio >= 4.0:         # ✅ dentro del for i
        print("Aprobado")
        aprobados += 1
    else:
        print("Reprobado")
        reprobados += 1

print(f"\n--- RESUMEN ---")     # 
print(f"Aprobados: {aprobados}")
print(f"Reprobados: {reprobados}")