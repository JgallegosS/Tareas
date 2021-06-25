# ESTRUCTURAS SELECTIVAS
class estructura_selectivas:
    def __init__(self):
        pass
    
    # ESTRUCTURAS SELECTIVAS SIMPLES
    def Ejer_Selectivas1(self):
        nota = float(input("Ingrese la calificación del examen: "))
        if nota >= 7:
            print("APROBADO con {} de puntaje" .format(nota))

    # ESTRUCTURAS SELECTIVAS DOBLES
    def Ejer_Selectivas2(self):
        nota = float(input("Ingrese la calificación del examen: "))
        if nota >= 7:
            print("APROBADO con {} de puntaje" .format(nota))
        else:
            print("REPROBADO con {} de punaje" .format(nota))

    def Ejer_Selectivas3(self):
        sueldo = float(input("Ingrese el sueldo: "))
        if sueldo <= 600:
            aumento = sueldo * 0.10
            Nuevo_sueldo = sueldo + aumento
            print("Su nuevo sueldo es {}" .format(Nuevo_sueldo))
        else:
            print("Su sueldo sigue siendo {}" .format(sueldo))

    #
    def Ejer_Selectivas4(self):
        horas_trabajadas, horas_extras, horas_extras_triple = 0, 0, 0
        valor_hora, pago_horas_extras, pago_total = 0, 0, 0
        horas_trabajadas = int(input("ingrese horas trabajadas: "))
        valor_hora = float(input("Ingrese el valor por hora: "))
        if (horas_trabajadas > 40):
            horas_extras = horas_trabajadas - 40
            if (horas_extras > 8):
                horas_extras_triple = horas_extras - 8
                pago_horas_extras = valor_hora * 2 * 8 + valor_hora * 3 * horas_extras_triple
            else:
                pago_horas_extras = valor_hora * 2 * horas_extras
            pago_total = valor_hora * 40 + pago_horas_extras
        else:
            pago_total = valor_hora * horas_trabajadas
        print("")
        print("")
        print("""
                Horas trabajadas: {} 
                Horas extras:     {} 
                Horas triple:     {}
                Valor Hora:       {} 
                Pago total:       {} """.format(horas_trabajadas, horas_extras, horas_extras_triple,
                                                valor_hora, pago_horas_extras, pago_total))
    def Ejer_Selectivas5(self):
        n1, n2, n3 = 0, 0, 0
        n1 = int(input("Ingerse numero 1"))
        n2 = int(input("Ingerse numero 2"))
        n3 = int(input("Ingerse numero 3"))
        if n1 > n2 > n3:
            print("El numero mayor es ", n1)
        elif n2 > n3 > n1:
            print("El numero mayor es: ", n2)
        else:
            print("El numero mayor es: ", n3)
    
    # ESTRUCTURAS SELECTIVAS MULTIPLES
    def Ejer_Selectivas6(self):
        valor1 = int(input("""Ingrese un opcion: 
        1 == mulriplicar por 100
        2 == potenciar por 100
        3 == dividir 100
        0 == Salir"""))
        valor2 = int(input("Ingrese otro valor: "))
        if valor1 == 1:
            respuesta = 100 * valor2
        elif valor1 == 2:
            respuesta = 100 ** valor2
        elif valor1 == 3:
            respuesta = 100/valor2
        else:
            respuesta = 0
        print("""El resultado del número {} y el valor {} es de: {} """.format(valor1, valor2, respuesta))
    
    # EXPRESIONES LOICAS  USE DE AND
    def Ejer_Selectivas7(self):
        nota1 = int(input("Ingrese la primera calificación: "))
        nota2 = int(input("Ingrese la segunda calificación: "))
        if nota1 >= 80 and nota2 >= 80:
            print("""La calificacion 1: {},la calificación 2:{} son mayores a 80 puntos
            FELICIDADES ES ACEPTADO""".format(nota1, nota2))
        else:
            print("""La calificacion 1: {},la calificación 2:{} son MENORES a 80 puntos
            UUSTED SERA RECHAZADO""".format(nota1, nota2))
if __name__ == "__main__":
    EstructurasSelectivas = estructura_selectivas()
    EstructurasSelectivas.Ejer_Selectivas1()
    EstructurasSelectivas.Ejer_Selectivas2()
    EstructurasSelectivas.Ejer_Selectivas3()
    EstructurasSelectivas.Ejer_Selectivas4()
    EstructurasSelectivas.Ejer_Selectivas5()
    EstructurasSelectivas.Ejer_Selectivas6()
    EstructurasSelectivas.Ejer_Selectivas7()
