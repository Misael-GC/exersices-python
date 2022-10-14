#Por buenas prácticas debes dejar 2 espacios entre cada función y en entry point o punto de entrada
def palindromo(palabra):
    palabra = palabra.replace(' ', '')#vamos a quitar los espacios
    palabra = palabra.lower()#pasar la palabra a minusculas
    palabra_invertida = palabra[::-1] #se guarda la palabra invertida
    if palabra == palabra_invertida:
        return True
    else:
        return False


#función que va a correr el programama al principio, es una buena práctica colocarla al principio
def run():
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra) #sea true o false se guarda en la variable
    if es_palindromo == True:
        print('Es palíndromo')
    else:
        print('No es palíndromo')


#punto de entrada de un programa de python, estandar,
if __name__ == '__main__':
    run()


#ejecutamos en consola py o python3 palindromo.py
