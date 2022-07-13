class Alumno:
    def __init__(self,alumno,nota):
        self.alumno = alumno
        self.nota = nota
    
    def getInfo(self):
        if self.nota < 5:
            return f'El nombre del alumno es: {self.alumno}, La nota del alumno es: {self.nota}', f'El alumno fue reprobado'
        else:
            return f'El nombre del alumno es: {self.alumno}, La nota del alumno es: {self.nota}', f'El alumno fue aprobado'
        


alumno1 = Alumno('vicente',4)
print(alumno1.getInfo())