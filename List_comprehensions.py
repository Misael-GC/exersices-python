def run():
    # squares = [] # en esta listas se agregaran las iteraciones 
    # for i in range(1, 101): 
    #     if i % 3 != 0: #si no es igual a 0 nos es divisible entre 3
    #         squares.append(i**2)  #el metodo append agregara las iteraciones al a lista

    #list comprehensions:
    squares = [i for i in range(1, 10000) if i % 4 == 0 if i % 6 == 0 if i % 9 == 0]

    print(squares)


if __name__ == '__main__':
    run()

