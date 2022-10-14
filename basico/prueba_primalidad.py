def es_primo(numero):
    contador = 0

    for i in range(1, numero+1): #numero + 1 para que tme al numero que queremos, en lugar de 99 si sea 99
        if i == 1 or i == numero:
            continue#saltate ese numero
        if numero % i == 0: #si no saltamos, entonces al dividir el numero el resultado es 0 aumenta 1 al contador
            contador += 1 #vamos aumentar 1 cuando el numero no sea primo, porque al dividir es cero no 1
    if contador == 0 :
        return True
    else:
        return False

def run():
    numero = int(input('Escribe un número: ')) #int volver a numero entero un string
    if es_primo(numero):
        print('Es primo')
    else:
            print('No es primo')

if __name__ == '__main__':
    run()


# ejecutemos en consola py o python3 archivo.py
#encuentra tu solución
