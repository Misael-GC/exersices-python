def run():
    my_list = [1, "Hello", True, 4.5] #lista
    my_dict = {"firstname": "Miguel", 'lastname': 'Rodriguez'}

    super_list = [
        {"firstname": "Miguel", 'lastname': 'Rodriguez'},
        {"firstname": "Miguel", 'lastname': 'Rodriguez'},
        {"firstname": "Miguel", 'lastname': 'Rodriguez'},
        {"firstname": "Miguel", 'lastname': 'Rodriguez'},
        {"firstname": "Miguel", 'lastname': 'Rodriguez'},
    ]

    super_dict = {
        'natural_nums': [1,2,3,4,5],
        'integer_nums': [-2,-1,0,1,2],
        'floating_nums': [1.1,4.5,6.43],
    }

    #metodo items() allow recorrer keys y values al mismo tiempo de un diccionario en un ciclo
    for key, value in super_dict.items():
        print(key, '-', value)


    for values in super_list:
        for key, value in values.items():
            print(f'{key} - {value}')


if __name__ == '__main__':
    run()