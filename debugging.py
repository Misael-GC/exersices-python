def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0: #si es el resultado es 1
            divisors.append(i) #lo agregamos
    return divisors

def run():
    num = int(input('ingresa un número: ')) #ingrese un numero y convertir a entero
    print(divisors(num))
    print('Terminó mi programa')

if __name__ == '__main__':
    run()