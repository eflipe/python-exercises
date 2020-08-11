from utils import database

MENU_PROMPT = "\n>>> '1' agregar nueva palabra, '2' mostrar lista de palabras, 'f' buscar una palabra" \
              ", 'd' borrar, 'q' salir." \
              "\n>>> "


def prompt_add_palabra():
    palabra = input('Palabra original: ')
    palabra_trad = input('Significado: ')
    frase = input('Frase ejemplo: ')
    frase_trad = input('Traducción frase: ')

    database.add_palabra(palabra, palabra_trad, frase, frase_trad)


def lista_palabras():
    dict_model = database.get_all()
    for palabra in dict_model:
        print_palabra(palabra)


def print_palabra(palabra):
    print(f'{palabra["palabra"]} : "{palabra["palabra_trad"]}"')
    print(f'{palabra["frase"]} : "{palabra["frase_trad"]}"')
    print(f'')


def buscar_palabra():
    search_palabra = input("Buscar palabra...")
    dict_model = database.get_all()
    for palabra in dict_model:
        if palabra['palabra_trad'] == search_palabra:
            print_palabra(palabra)


def borrar_palabra():
    name = input("Palabra a eliminar: ")
    database.delete_palabra(name)


user_options = {
    '1': prompt_add_palabra,
    '2': lista_palabras,
    'f': buscar_palabra,
    'd': borrar_palabra
}


def menu():
    # database.create_table()
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection in user_options:
            selected_function = user_options[selection]
            selected_function()
        else:
            print("Error. ")

        selection = input(MENU_PROMPT)


menu()
