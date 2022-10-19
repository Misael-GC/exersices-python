#1 importamos lo que vamos a necesitar
import random
import os


#2 creamos la función que nos traiga las palabras del archivo de texto y lo metemos en una lista
def word():
    with open("./archivo/data.txt", 'r', encoding='utf-8') as f:
        words = [line for line in f]
    word_random = (random.choice(words)).strip().upper() #elegit una palabra y convertirla a minusculas, quitar los esppacios
    return word_random


#mostramos en una lista las longitud de _ que imprimira en pantalla _ _ _ _ _
def long_word():
    len_word = len(word)-1
    presentation = ['_ ']*len_word
    return presentation


# ocultar las palabras
def changelarg(hidden_word, letter, index):
    hidden_word[index] = letter
    return hidden_word

#imprimir las vidas en pantalla
def print_scan(lifes):
    print('='*20 + ' Welcome to Hangman Game ' '='*20)
    list_ascii = [''' 
                   +-----+
                        ||
                        ||
                        ||
                        ||
                        ||
                  ========= ''', '''
                  +------+
                    |   ||
                        ||
                        ||
                        ||
                        ||
                  ========= ''', '''
                    +----+
                    |   ||
                   😮   |
                        ||
                        ||
                        ||
                  ========= ''', '''
                    +----+
                    |   ||
                   😖   |
                    |   ||
                        ||
                        ||
                  ========= ''', '''
                    +----+
                    |   ||
                   😨   |
                   /|   ||
                        ||
                        ||
                  ========= ''', '''
                    +----+
                    |   ||
                   🥴   |
                   /|\  ||
                        ||
                        ||
                  ========= ''', '''
                    +----+
                    |   ||
                   😵‍💫   |
                   /|\  ||
                   /    ||
                        ||
                  ========= ''', '''
                    +---+
                    |   |
                   😵   |
                   /|\  |
                   / \  |
                        |
                  =========
                  ''']
    
    list_ascii = list_ascii[::-1]  
    print(list_ascii)
    
#definir configuraciones de inicio, variables que va a llamar funciones, y valores
def play():
    select_word = word() #llamamos a la función word para traer una palabra random
    large = long_word(select_word) # en pantalla _ _ _ _ _
    
    hits = 0
    objetive = len(select_word)-1 #no muesatre la palabra completa sino que falte 1
    lifes = 6
    usedletters = []
    
    
    while lifes > 0 and hits < objetive: #while vidas > 0 y intentos < longitud
        print_scan(lifes)
        print('')
        print("Adivine la siguiente palabra. La misma cuenta con " +
              str(len(select_word)-1)+" caracteres.")
        print(*large, sep=' ')
        print('')
        letter = input('Ingrese una letra: ').upper()
        assert letter.isalpha(), 'Debe introducir una letra. No números'
        
        
        while len(letter) != 1:
            letter = input('Ingreso más de un dígito: ').upper()
            assert letter.isalpha(), 'Debe introducir una letra. No números'
        
        
        while letter in usedletters:
            letter = input(' "Ingresó una letra repetida. Ingrese otra que no haya usado: ').upper()
            usedletters.append(letter)
            print("Las letras usadas hasta aquí son: ")
            print(*usedletters, sep=' ')
            hitsbefore = hits
            
            
            for i in range(0, len(select_word)-1):
                if select_word[i] == letter:
                    hits += 1
                    print('Excelente. Ha acertado! Ha sumado 1 punto. Quedan ' + str(objetive-hits) + ' letras por encontrar')
                    large = changelarg(large, letter, i)
                    
            if hitsbefore == hits:
                lifes -= 1
                print( "No se encontró la letra elegida. Usted ha perdido una vida. Le quedan: "+ str(lifes) + ' vidas')
                
                input('Presiona Enter para continuar: ')
                os.system('cls') 
                
            if hits == objetive:
                print_scan(lifes)
                print('''
                    ────────────────────░███░
                    ───────────────────░█░░░█░
                    ──────────────────░█░░░░░█░
                    ─────────────────░█░░░░░█░
                    ──────────░░░───░█░░░░░░█░
                    ─────────░███░──░█░░░░░█░
                    ───────░██░░░██░█░░░░░█░
                    ──────░█░░█░░░░██░░░░░█░
                    ────░██░░█░░░░░░█░░░░█░
                    ───░█░░░█░░░░░░░██░░░█░
                    ──░█░░░░█░░░░░░░░█░░░█░
                    ──░█░░░░░█░░░░░░░░█░░░█░
                    ──░█░░█░░░█░░░░░░░░█░░█░
                    ─░█░░░█░░░░██░░░░░░█░░█░
                    ─░█░░░░█░░░░░██░░░█░░░█░
                    ─░█░█░░░█░░░░░░███░░░░█░
                    ░█░░░█░░░██░░░░░█░░░░░█░
                    ░█░░░░█░░░░█████░░░░░█░
                    ░█░░░░░█░░░░░░░█░░░░░█░
                    ░█░█░░░░██░░░░█░░░░░█░
                    ─░█░█░░░░░████░░░░██░
                    ─░█░░█░░░░░░░█░░██░█░
                    ──░█░░██░░░██░░█░░░█░
                    ───░██░░███░░██░█░░█░
                    ────░██░░░███░░░█░░░█░
                    ──────░███░░░░░░█░░░█░
                    ──────░█░░░░░░░░█░░░█░
                    ──────░█░░░░░░░░░░░░█░
                    ──────░█░░░░░░░░░░░░░█░
                    ──────░█░░░░░░░░░░░░░█░
                    ████──░█░████░░░░░░░░█░
                    █──█──████──████░░░░░█░
                    █──█──█──█──█──████████
                    █──█──████──█──█──────█
                    █──█──█──█────██──██──█
                    █──████──█──█──█──────█
                    █─────█──█──█──█──█████
                    ███████──████──█──────█
                    ──────████──██████████
                    ★══════════★★══════════★
                      ''')
                
            
            if lifes == 0:
                print_scan(lifes)
                print('''
                      ⠄⢀⣀⣤⣴⣶⣶⣤⣄⡀⠄⠄⣀⣤⣤⣤⣤⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
                    ⣴⣏⣹⣿⠿⠿⠿⠿⢿⣿⣄⢿⣿⣿⣿⣿⣿⣋⣷⡄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
                    ⣿⢟⣩⣶⣾⣿⣿⣿⣶⣮⣭⡂⢛⣭⣭⣭⣭⣭⣍⣛⣂⡀⠄⠄⠄⠄⠄⠄⠄⠄
                    ⣿⣿⣿⣿⡿⢟⣫⣭⣷⣶⣾⣭⣼⡻⢛⣛⣭⣭⣶⣶⣬⣭⣅⡀⠄⠄⠄⠄⠄⠄
                    ⣿⡿⢏⣵⣾⣿⣿⣿⡿⢉⡉⠙⢿⣇⢻⣿⣿⣿⣿⡟⠉⠉⢻⡷⠄⠄⠄⠄⠄⠄
                    ⣿⣷⣾⣍⣛⢿⣿⣿⣿⣤⣁⣤⣿⢏⠸⣿⣿⣿⣿⣷⣬⣥⣾⠁⣿⣿⣷⠄⠄⠄
                    ⣿⣿⣿⣿⣭⣕⣒⠿⠭⠭⠭⡷⢖⣫⣶⣶⣬⣭⣭⣭⣭⣥⡶⢣⣿⣿⣿⠄⠄⠄
                    ⣿⣿⣿⣿⣿⣿⣿⡿⣟⣛⣭⣾⣿⣿⣿⣝⡛⣿⢟⣛⣛⣁⣀⣸⣿⣿⣿⣀⣀⣀
                    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                    ⣿⡿⢛⣛⣛⣛⣙⣛⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣬⣭⣭⠽⣛⢻⣿⣿⣿⠛⠛⠛
                    ⣿⢰⣿⣿⣿⣿⣟⣛⣛⣶⠶⠶⠶⣦⣭⣭⣭⣭⣶⡶⠶⣾⠟⢸⣿⣿⣿⠄⠄⠄
                    ⡻⢮⣭⣭⣭⣭⣉⣛⣛⡻⠿⠿⠷⠶⠶⠶⠶⣶⣶⣾⣿⠟⢣⣬⣛⡻⢱⣇⠄⠄
                    ⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⠶⠒⠄⠄⠄⢸⣿⢟⣫⡥⡆⠄⠄
                    ⢭⣭⣝⣛⣛⣛⣛⣛⣛⣛⣿⣿⡿⢛⣋⡉⠁⠄⠄⠄⠄⠄⢸⣿⢸⣿⣧⡅⠄⠄
                    ⣶⣶⣶⣭⣭⣭⣭⣭⣭⣵⣶⣶⣶⣿⣿⣿⣦⡀⠄⠄⠄⠄⠈⠡⣿⣿⡯⠁⠄⠄
`7MMMMMMq.`7MMMMMYMM  `7MMMMMMMq.  `7MMMMMYb.`7MMF' .MMMMbgd MMP""MM""YMM `7MMMMMYMM  
  MM   `MM. MM    `7    MM   `MM.   MM    `Yb. MM  ,MI    "Y P'   MM   `7   MM    `7  
  MM   ,M9  MM   d      MM   ,M9    MM     `Mb MM  `MMb.          MM        MM   d    
  MMmmdM9   MMmmMM      MMmmdM9     MM      MM MM    `YMMNq.      MM        MMmmMM    
  MM        MM   Y  ,   MM  YM.     MM     ,MP MM  .     `MM      MM        MM   Y  , 
  MM        MM     ,M   MM   `Mb.   MM    ,dP' MM  Mb     dM      MM        MM     ,M 
.JMML.    .JMMmmmmMMM .JMML. .JMM..JMMmmmdP' .JMML.P"Ybmmd"     .JMML.    .JMMmmmmMMM 
_____________________________________________________________________________________
                      ''')
    
    

# 0 - configuación inicial
def run():
    play()


if __name__ == '__main__':
    run()