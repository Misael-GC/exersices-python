import random


def generate_password():
    #generar 4 listas de simbolos que se van a combinar
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    simbolos = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']

    # unimos las listas
    caracteres = mayusculas + minusculas + simbolos + numeros

    #caracteres random
    password = []

    # mientras la longitud sea menor a 16
    while (len(password)<16): #tambien puede ser -> for i in range(15)
        # con choice se elige un caracter al azar, choice es funcion especial que pértenece a random
        caracteres_random = random.choice(caracteres)
        password.append(caracteres_random) # agregamos a la lista con los 15 caracteres


    #vamos a convertir nuestra lista a string
    password = ''.join(password) #vamos a unir toda la lista en una sola cadena
    return password


def run():
    password = generate_password()
    print('Your new password is: ' + password)


if __name__ == '__main__':
    run()