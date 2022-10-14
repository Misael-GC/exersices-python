import random


def run():
    numero_aleatorio = random.randint(1, 100) #randint-> numero entero aleatorio
    numero_elegido = int(input('Elige un número del 1 al 100: '))
    while numero_elegido != numero_aleatorio: #mientras sea diferentes ejecutamos una vuelta al ciclo
        if numero_elegido < numero_aleatorio: #si n elegido sea menor
            print('Busca un numero más grande')
        else:
            print('Busca un numero más pequeño')
        numero_elegido = int(input('Elige otro número: ')) #despues de los avisos vuelve a intentar con otro numero
    print('Ganaste!!!')


if __name__ == '__main__':
    run()