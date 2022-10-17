from multiprocessing.sharedctypes import Value


def divisors(num):
    try:
        if num < 0 or num == 0:
            raise ValueError('No se puede ingresar un número negativo')
        divisors = [i for i in range(1, num + 1) if num % i == 0]
        #   for i in range(1, num + 1):
        #   if num % i == 0: #si es el resultado es 1
        #     divisors.append(i) #lo agregamos
        return divisors
    except ValueError as ve:
        print(ve)
        print('ingresa un número positivo')
        return False

def run():
        num = input('ingresa un número: ') #ingrese un numero y convertir a entero
        assert num.isnumeric(), 'Debes ingresar un número entero y que no sea negativo' #.isnumeric -> metodo dice es un numero?
        print(divisors(int(num))) #volvemos a num en un entero
        print('Terminó mi programa')

if __name__ == '__main__':
    run()