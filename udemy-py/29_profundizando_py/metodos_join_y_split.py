# help(str.join)
tupla_str = ("Hola", "Mundo", "Como estas?")

mensaje_join = ' '.join(tupla_str)
print(mensaje_join)
mensaje_join = ','.join(tupla_str)
print(mensaje_join)
mensaje_join = '.'.join("adidas")
print(mensaje_join)
diccionario = {
    'nombre': 'Hector',
    'apellido': "Peres"
}
llaves = '-'.join(diccionario.keys())
valores = '-'.join(diccionario.values())
print(llaves)
print(valores)

# split: convertir una cadena en una lista
# help(str.split)
lista_str = "Hola mundo como estas todo bien"
lista_split = lista_str.split('o')
print(lista_split)
lista_split = lista_str.split('do')
print(lista_split)
lista_str = "Hola,mundo,como,estas,todo,bien"
lista_split = lista_str.split(',')
print(lista_split)
