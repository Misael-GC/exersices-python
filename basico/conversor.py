def conversor(tipo_pesos, valor_dolar):
    pesos = input('¿Cuántos pesos ' + tipo_pesos + ' tienes?')
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2) #permitir el numero de decimales en este caso 4
    dolares = str(dolares) #antes de imprimir lo convertimos en string
    print('Tienes $' + dolares + ' dólares')

#salto de linea con triple commillas
menu = '''
Bienvenido al conversor de monedas 💰

1- COL
2 - ARG
3- MXN

Elige la opción:
'''
opcion = int(input(menu))

if opcion == 1:
    conversor('colombianos', 3875)

elif opcion == 2:
    conversor('argentinos', 120)

elif opcion ==3:
    conversor('mexicanos', 20)
else:
    print('elige una opcion correcta')



# ejecutamos python3 conversor.py en la consola o py conversor.py
