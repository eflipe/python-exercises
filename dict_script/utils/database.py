import json

'''
[
    {
        'palabra': palabra,
        'palabra_trad': palabra_trad,
        'frase': frase,
        'frase_trad': frase_trad
    }
]
'''


dict_model = 'dict_project.json'


def create_table():
    with open(dict_model, 'w') as file:
        json.dump([], file)


def add_palabra(palabra, palabra_trad, frase, frase_trad):
    dict_json = get_all()
    dict_json.append(
    {
        'palabra': palabra,
        'palabra_trad': palabra_trad,
        'frase': frase,
        'frase_trad': frase_trad
    }
    )
    _save_all(dict_json)
    # with open(dict_model, 'a') as file:
    #     file.write(f'{palabra},{palabra_trad},{frase},{frase_trad}\n')

    # dict_model.append(
    #     {
    #         'palabra': palabra,
    #         'palabra_trad': palabra_trad,
    #         'frase': frase,
    #         'frase_trad': frase_trad
    #     }
    # )

def get_all():
    with open(dict_model, 'r') as file:
        return json.load(file)
    #     lines = [line.strip().split(',') for line in file.readlines()]
    # dict_m = [
    #     {
    #      'palabra': line[0],
    #      'palabra_trad': line[1],
    #      'frase': line[2],
    #      'frase_trad': line[3]
    #     } for line in lines
    # ]
    # return dict_m

def _save_all(dict_m):
    with open(dict_model, 'w') as file:
        json.dump(dict_m, file, ensure_ascii=False)

def delete_palabra(name):
    dict_palabras = get_all()
    print(dict_palabras)
    print(name)
    dict_palabras = [palabra for palabra in dict_palabras if palabra['palabra_trad'] != name]
    print(f"Se borró {name} ")
    _save_all(dict_palabras)

    # global dict_model
    # dict_model = [palabra for palabra in dict_model if palabra['name'] != name]

    # for palabra in dict_model:
    #     if palabra['name'] == name:
    #         dict_model.remove(palabra)
