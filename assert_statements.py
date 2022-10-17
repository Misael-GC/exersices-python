from multiprocessing.sharedctypes import Value


def divisors(num):
        divisors = [i for i in range(1, num + 1) if num % i == 0]
        #   for i in range(1, num + 1):
        #   if num % i == 0: #si es el resultado es 1
        #     divisors.append(i) #lo agregamos
        return divisors

def run():
        num = int(input('ingresa un número: ')) #ingrese un numero y convertir a entero
        assert num > 0, 'Debes ingresar un número positivo' #.isnumeric -> metodo dice es un numero?
        print(divisors(num)) #volvemos a num en un entero
        print('Terminó mi programa')

if __name__ == '__main__':
    run()