# Unpacking - desempaquetado
valores = 1,2,3
print(valores)
print(type(valores))

valor1, valor2, valor3 = 1, 2, 3
print(valor1, valor2, valor3)

valor1, _, valor3 = 1, 2, 3  # '_' es una variable que no vamos a utilizar
print(valor1, valor3)

valor1, valor2, *valor3 = 1, 2, 3, 4, 5, 6, 7, 8, 9  # el valor3, ahora es una lista
print(valor1, valor2, valor3)

valor1, valor2, *valor3, valor4, valor5 = 1, 2, 3, 4, 5, 6, 7, 8, 9  # *valor3 almacena los valores restantes
print(valor1, valor2, valor3, valor4, valor5)

valor1, *valor33 = 1, 2, 3, 4, 5, 6, 7, 8, 9
print('Otro', valor1, valor33)

def regresa_varios_datos():
    return (1, 2, 3)

valor1, valor2, valor3 = regresa_varios_datos()
print(valor1, valor2, valor3)

valor1, *valores_restantes = regresa_varios_datos()
print(valor1, valores_restantes)

# help(str.partition)
hora, _, minutos = '04:20'.partition(':')
# print(type(variable))
print(hora, minutos)
