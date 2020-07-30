def ord_insercion(lista):
    "Ordena una lista según el método de inserción"
    for i in range(len(lista) - 1):
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        print(f'{lista[i+1]} es menor que {lista[i]}?? ')
        if lista[i+1] < lista[i]:
            print(f'SI')
            reubicar(lista, i + 1)
        else:
            print(f'NO')
        print("DEBUG: ", lista)


def reubicar(lista, p):
    """Reubica al elemento que está en la posición p de la lista
    dentro del segmento [0:p-1]."""

    v = lista[p]
    print(f"Valor lista[p] = {lista[p]}")
    # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j].
    j = p
    print(f'Posicion J = {p}')
    print(f'Valor lista[j - 1]: {lista[j - 1]}')
    print("---Empieza el while---")
    while j > 0 and v < lista[j - 1]:
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        print(f'Valor lista[v]: {lista[v]}')
        print(f'Valor lista[j]: {lista[j]}')
        print(f'Valor lista[j-1]: {lista[j-1]}')
        print(f'Reemplazo Valor lista[j]: {lista[j]} por Valor lista[j-1]: {lista[j-1]}')
        lista[j] = lista[j - 1]

        print(f'J = {j}')
        j -= 1
        print(f'J = {j}')
    print("---While finalizado---")

    lista[j] = v
    print(f"V: {v}")


lista = [3, 2, -1, 5, 0, 2]
ord_insercion(lista)
