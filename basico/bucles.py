# def run(num, rept):
#     if num <= rept:
#         cont = num
#         print(str(2 ** cont) )
#         run(num+1, rept)
#     else:
#         print("Fin!")

# if __name__ == "__main__":
#     repeticiones = int(input("Cuantas potencias: "))
#     run(0, repeticiones)


def run():
    LIMITE = 1000 #para poner constantes en python es con mayusculas
    contador = 0 #variable que va a cambiar si el contador es 3 -> 2*2*2
    potencia_2 = 2**contador #2**0 =1
    while potencia_2 < LIMITE: #mientras se cumpla la condición -> 1 < 1000
        print('2 elevado a ' + str(contador) + ' es igual a:' + str(potencia_2))
        contador = contador + 1 #vamos sumando de a 1 a contador -> 0+1 =1....
        potencia_2 = 2**contador #2**1 = 2


if __name__ == '__main__':
    run()

#py or python3 bucle.py
