import numbers
from unicodedata import name


def read(): #leer del 1 al 10, y convertirla en una lista
    numbers = [] 
    with open('./archivo/texto.txt', 'r', encoding='utf-8') as f:
        for line in f:
            numbers.append(int(line))
    print(numbers) #del archivo.txt itera cada item y lo mete en una lista


def write():
    names = ['Facundo', 'Miguel', 'Pepe', 'Chema', 'Rocío']
    with open('./archivo/names.txt', 'w', encoding='utf-8') as f: #f es una variable que representa a la conexion de python con nuestro file y tiene varios metodos, uno se llama write
        for name in names:
            f.write(name)
            f.write("\n")#creamos un nuevo archivo con los nombres en columna


def run():
    #read()
    write()


if __name__ == '__main__':
    run()
   
   
    
# # utf-8 todo lo que se escriba no tenga caracteres extraños, como la ñ o tildes