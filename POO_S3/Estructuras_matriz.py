import numpy as np


class Matrices:
    exam = np.ones((30, 6))

    def __init__(self, prom_exam=0):
        self.prom_exam = prom_exam

    def Promedio_examenes_materia(self):
        for j in range(0, 6):
            for i in range(0, 30):
                nota = float(input("Ingrese la nota examen del alumno {} de la materia {}:".format((i+1), (j+1))))
                self.exam[i, j] = nota

        # cálculo del promedio de calificaciones de cada uno de los exámenes
        self.prom_exam = []
        print("")
        print("")
        for j in range(0, 6):
            acum = 0
            for i in range(0, 30):
                num = self.exam[i, j]
                acum = acum + num
            prom = acum/30
            self.prom_exam.append(prom)
            print("Promedio de examenes de la materia {}, es de {}".format(j+1, prom))
        return self.prom_exam

    def Promedio_cada_alumno(self):
        print("")
        print("")
        for i in range(0, 30):
            acum = 0
            for j in range(0, 6):
                num = self.exam[i, j]
                acum = acum + num
            prom = acum/6
            print("Promedio del alumno {}, es {}".format(i+1, prom))

    def Puntaje_mayor_examen(self):
        print("")
        print("")
        Examen = 1
        examenes = self.prom_exam
        mayor = examenes[0]
        for i in range(1, 6):
            if mayor < examenes[i]:
                mayor = examenes[i]
                Examen = i
        print("El examen {}, obtuvo el mayor promedio con : {}".format(Examen, mayor))


if __name__ == "__main__":
    Curso = Matrices()
    Curso.Promedio_examenes_materia()
    Curso.Promedio_cada_alumno()
    Curso.Puntaje_mayor_examen()
