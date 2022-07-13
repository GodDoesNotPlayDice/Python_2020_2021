alumnos = [['Alberto Gonzalez', 40, 30, 70], ['Francisca Almonacid', 100, 40], ['Pedro Reyes', 30, 50], ['Juan Campos', 30, 60, 30, 70], ['Andrea Zamora', 30]]
def calcular_promedio(alumnos):
    for i in alumnos:
        a = 0
        for x in i[1:]:
            a+=x
            print(a)


calcular_promedio(alumnos)