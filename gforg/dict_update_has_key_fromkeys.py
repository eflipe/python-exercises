# fromkeys(seq, value):
# crea un nuevo dic

dic_1 = {
    'Name': 'Pepe',
    'Age': 200
}

dic_2 = {
    'ID': 73783287328732,
    'Tel': 1532233
}

sequ_1 = ('Name', 'Age', 'ID', 'Tel')

#update()

dic_1.update(dic_2)
print(f'new dic: {str(dic_1)}')

#fromkeys(sequ, VALOR)
dict_fromkeys = dict.fromkeys(sequ_1, 'pepe')
print(str(dict_fromkeys))

#has_key() True si existe
#get(key, val) si la key no existe, devuelve val

if not 'pepe' in dic_1:
    print('No tiene')

if 'ID' in dic_1:
    print('tiene')

print(dic_1.get('pepe', "no existe"))

print(dic_1.setdefault('pepe', "nuevo valor creado"))
print(f'new dic: {str(dic_1)}')