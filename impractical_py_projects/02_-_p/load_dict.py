'''
Convierte un archivo de texto en una lista.

Argumentos:
- El nombre del archivo de texto (y la dirección del path)

Exceptiones:
-IOError si el archivo no es encontrado

Returns:
- Una lista de todas las palabras en minúsculas.

Requerimientos:
- import sys
'''

import sys


def load(file):
    """Abre un archivo de texto y devuelve una lista"""
    try:
        with open(file, encoding='utf8') as f:
            loaded_txt = f.read().strip().split('\n')
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print("{}\nError al abrir {}.".format(e, file))
        sys.exit(1)
