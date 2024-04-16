asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []
for asignatura in asignaturas:
    nota = input(f"Ingrese la nota que ha sacado en {asignatura}: ")
    notas.append(nota)
for i in range(len(asignaturas)):
    print(f"En {asignaturas[i]} has sacado {notas[i]}")
