import sys
from collections import Counter
import load_dict

dict_file = load_dict.load('X')
dict_file = sorted(dict_file)

ini_name = input("Enter a name: ")
print(f'\nDEBUG: primer frase del usuario: {ini_name}\n')


def find_anagrams(name, word_list):
    name_letter_map = Counter(name)
    print(f'\nDEBUG: contador: {name_letter_map}\n')

    anagrams = []

    for word in word_list:
        test = ''
        word_letter_map = Counter(word.lower())
        for letter in word:
            if word_letter_map[letter] <= name_letter_map[letter]:
                test += letter
        if Counter(test) == word_letter_map:
            print(f'\nDEBUG: anagrama encontrado: {word_letter_map}\n')
            print(f'\nDEBUG: palabra agregada: {word}\n')

            anagrams.append(word)
    print(*anagrams, sep='\n')
    print()
    print("Letras restantes = {}".format(name))
    print("Cantidad de letras restantes = {}".format(len(name)))
    print("Cantidad restante de anagrama = {}".format(len(anagrams)))


def process_choice(name):
    print('DEBUG: users choice word: {}'.format(name))
    while True:
        choice = input('\nMake a choice else Enter to start over or "#" to end:' )
        if choice == '':
            main()
        elif choice == '#':
            sys.exit()
        else:
            candidate = ''.join(choice.lower().split())
            print('DEBUG: la eleccion(candidate) del usuario(?): {}'.format(candidate))
        left_over_list = list(name)
        print('DEBUG: left_over_list(la palabra del usuario): {}'.format(left_over_list))

        for letter in candidate:
            if letter in left_over_list:
                left_over_list.remove(letter)
                print('DEBUG: left_over_list(la palabra del usuario): {}'.format(left_over_list))

        if len(name) - len(left_over_list) == len(candidate):
            break
        else:
            print("No va a funcionar, hace otra elección")
    name = ''.join(left_over_list)
    return choice, name


def main():
    name = ''.join(ini_name.lower().split())
    name = name.replace('-', '')
    limit = len(name)
    phrase = ''
    running = True

    while running:
        temp_phrase = phrase.replace(' ', '')
        if len(temp_phrase) < limit:
            print("Longitud del anagrama = {}".format(len(temp_phrase)))

            find_anagrams(name, dict_file)
            print("DEBUG: Llamamos a la funcion find_anagrams()")
            print("Current anagram phrase=", end="")
            print(phrase)

            print("DEBUG: Llamamos a la funcion process_choice()")
            choice, name = process_choice(name)
            phrase += choice + ' '

        elif len(temp_phrase) == limit:
            print("\n****FIN!!!!*****\n")
            print("Anagrama =", end="")
            print(phrase)
            print()
            try_again = input('\n\nTry again?("#" para salir)\n')
            if try_again.lower() == "#":
                running = False
                sys.exit()
            else:
                main()


if __name__ == '__main__':
    main()
