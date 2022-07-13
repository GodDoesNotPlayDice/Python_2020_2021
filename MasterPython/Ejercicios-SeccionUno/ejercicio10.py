"""
    Ejercicio10. El programa tiene que pedir la nota de 15 alumnos de cuantos han aprobado y cuantos han sido rechazados

"""
n = 1
a = 0
r = 0
while n < 5+1:
    alumno = str(input(f'Dame el nombre del alumno numero {n}: '))
    nota = int(input(f'Dame la calificacion del alumno {alumno}: '))
    if nota < 5:
        print(f'{alumno} con nota {nota} ha sido Reprobado!')
        r += 1
    elif nota >= 5:
        print(f'El almuno {alumno} con nota {nota} ha sido Promovido!')
        a += 1
    n+=1
print(f"Alumnos Aprobados: {a} \nAlumnos Reprobados: {r}")

