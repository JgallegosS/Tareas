class Es_Ciclicas:
    def __init__(self):
        pass
    
    # ESTRUCTURAS FOR
    def For1(self):
        acu = 0
        for i in range(0, 100):
            acu += i
        print("Suma de los 100 primeros números es: {}".format(acu))

    # Bucles anidados
    def For2(self):
        num = int(input("Ingrese un número: "))
        factorial = 0
        multiplicador = num
        for i in range(1, num+1):
            multiplicador -= 1
            factorial = num * multiplicador

        print("El factorial del número {} es: {}" .format(num, factorial))
    
    #ESTRUCTURAS WHILE CONTROLADO POR CONTADOR
    def While1(self):
        i = 1
        print("Contador números hasta el 100:")
        while i <= 100:
            print(i)
            i +=1

    #BUCLE WHILE CONTROLADO POR CONDICION
    def While2(self):
        suma = 0
        producto = 1
        respuesta = "S"
        while respuesta == "S":
            n = int(input("Ingrese un número: "))
            suma = suma + n
            producto = producto * n
            print("El total de la suma es: {}" .format(suma))
            print("El total del producto es: {}" .format(producto))
            print("Desea continuar [S/N]:  ")
            respuesta = input().capitalize()

    #BUCLE CONTROLADO POR CONDICION #2
    def While3(self):
        suma = 0
        prod = 1
        n = 0
        while n != -1:
            numero = int(input("Ingrese un número: "))
            suma = suma + numero
            producto = prod * numero
            print("El total de la suma es: {}" .format(suma))
            print("El total del producto es: {}" .format(producto))
            print("")

    # BUCLE CONTROLADO POR BANDERAS O INTERRUPTORES
    def While4(self):
        bandera = True
        divisor =2
        numero = int(input("Ingrese un número: "))
        while divisor < numero and bandera == True:
            res = numero % divisor
            if res == 0:
                bandera = False
            divisor += 1
        if bandera == True:
            print("El número {} es primo" .format(numero))
        else:
            print("El número {} no es primo" .format(numero))
    
    #ESTRUCTURAS REPEAT
    def While5(self):
        serie = 0
        I = 0
        numero = int(input("Ingrese un número: "))
        bandera =True
        while bandera:
            if bandera == True:
                serie = serie+(1/I)
                bandera = False
            else:
                serie = serie-(1/I)
                bandera = True
            I += 1
            if I > numero:
                break
            print("El resultado de la serie es : {}" .format(serie))

if __name__ == "__main__":
    ciclos = Es_Ciclicas()
    ciclos.For1()
    ciclos.For2()
    ciclos.While1()
    ciclos.While2()
    ciclos.While3()
    ciclos.While4()
    ciclos.While5()
