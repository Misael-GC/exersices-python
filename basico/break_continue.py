# vamos a imprimir solo los numeros pares
def run():
    # for contador in range(100):
    #     if contador % 2 != 0: #si al dividir entre 2 es diferente a cero, saltatelo
    #         continue #y lo que este debajo de continue no se va a ejecutar
    #     print(contador)
    # vamos a ejecutar hasta 5678
    # for i in range(10000):
    #     print(i)
    #     if i == 5678:
    #         break

#romper ciclo hasta que nos encontrmos con la letra o
    # texto = input('Escribe un texto: ')
    # for letra in texto:
    #     if letra == 'o':
    #         break
    #     print(letra)

    #imprimir de 1 a 1000

    contador = 1
    print(contador)
    while contador < 1000:
        contador = contador + 1 #atajo contador +=1
        if contador % 2 != 0:
            continue
        if contador == 50:
            break
        print(contador)

# py for.py

if __name__ == '__main__':
    run()
