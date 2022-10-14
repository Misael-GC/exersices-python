import random


def run():
    numero_aleatorio = random.randint(1, 15)
    numero_elegido = int(input('Elige un número del 1 al 15: '))
    while numero_elegido != numero_aleatorio:  #mientras sea diferentes
        if numero_elegido < numero_aleatorio:  #si n elegido sea menor
            print(f'{random.randint(1, 15)} es tu asiento, si ya son 3 asientos ocupados, porfavor vuelve a presionar el mismo numero u del 1 - 15. Caliente')
        else:
            print(f'{random.randint(1, 15)} es tu asiento. si ya son 3 asientos ocupados, porfavor vuelve a presionar el mismo numero u del 1 - 15. Frio')
        numero_elegido = int(
            input('Elige otro número: '))  #despues de los avisos vuelve a intentar con otro numero
    print('Ganaste!!!')


if __name__ == '__main__':
    run()
