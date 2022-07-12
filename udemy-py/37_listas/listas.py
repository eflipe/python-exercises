lista_1 = ['elemento_1', 'elemento_2', 'elemento_3', 'elemento_4']
lista_2 = 'elemento_1, elemento_2, elemento_3, elemento_4'.split()  # split() devuelve una lista
numeros1 = [10, 40, 15, 4, 20, 90, 4]

# sumar una lista
listas_sumadas = lista_1 + lista_2
print("Lista sumada: ", listas_sumadas)
# extender una lista
lista_1.extend(lista_2)
print("Lista_1 extendida:", lista_1)

numeros_1 = [1, 2, 3, 4, 5, 6, 2]
# obtener el indice del primer elemento encontrado en una lista
print("Indice elemento 2:", numeros_1.index(2))

# invertir orden
numeros_1.reverse()
print("Lista invertida:", numeros_1)
print("Indice elemento 2:", numeros_1.index(2))

# ordenar
numeros_1.sort()
print(numeros_1)
# desc
numeros_1.sort(reverse=True)
print(numeros_1)

# copiar los elementos de una lista
copia_numero_1 = numeros_1.copy()  # shallow copy

# con slice
numeros_2 = numeros_1[:]

# Copiar los elementos de una lista
numeros2 = numeros1.copy()
# help(list.copy)
print(f'Misma referencia? {numeros1 is numeros2}')
print(f'Mismo contenido? {numeros1 == numeros2}')

# Podemos usar el constructor de la lista
numeros2 = list(numeros1)
print(f'Misma referencia? {numeros1 is numeros2}')
print(f'Mismo contenido? {numeros1 == numeros2}')

# slicing
numeros2 = numeros1[:]
print(f'Misma referencia? {numeros1 is numeros2}')
print(f'Mismo contenido? {numeros1 == numeros2}')

# matrices: una lista de listas es una matriz
# Matrices en Python
matriz = [[10, 20], [30, 40, 50], [60, 70, 80, 90]]
print(f'Matriz original: {matriz}')
print(f'Renglón 0, Columna 0: {matriz[0][0]}')
print(f'Renglón 2, Columna 3: {matriz[2][3]}')
matriz[2][0] = 65
print(f'Matriz modificada: {matriz}')

# order listas

lista_listas = [[10,14,87,90,71],[4,5,6,7],[9,0,11,15,45,61,70]]
lista_listas.sort(key=len)
print(f'Ordenar lista: {lista_listas}')

# sorted built-in
# help(sorted)
nombres1 = ['Juan Carlos', 'Karla', 'Pedro', 'Esperanza']
nombres1 = sorted(nombres1)
print(nombres1)
# ordenar de manera descendente
nombres1 = sorted(nombres1, reverse=True)
print(nombres1)
# Ordenar por la cantidad de caracteres (largo)
nombres1 = sorted(nombres1,key=len)
print(nombres1)
# built-in reversed
nombres1 = reversed(nombres1)
print(list(nombres1))
