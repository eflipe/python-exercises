# handle missing keys


# using get()
'''
get(key, def_val) -> def_val: valor que nos devuelve se la key NO existe
'''

# setfefault()
'''
setdefault(key, def_value) -> crea def_value no NO existe la key
'''

# defaultdict (from collections)
import collections

default_dict = collections.defaultdict(lambda: 'Valor default')

default_dict['a'] = 1
default_dict['b'] = 2

print('El valor con la letra C es: ', end='')
print(default_dict['c'])
