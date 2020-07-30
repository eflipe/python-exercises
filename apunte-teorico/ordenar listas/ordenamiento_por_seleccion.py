def ord_seleccion(lista):

    # posicion final del segmento/lista a tratar
    n = len(lista) - 1

    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        p = buscar_max(lista, 0, n)
        # intercambiar el valor que está en p con el valor que
        # está en la última posición del segmento
        lista[p], lista[n] = lista[n], lista[p]
        print("DEBUG", p, n, lista)

        # reducir el segmento en 1
        n = n - 1


def buscar_max(lista, a, b):
    """
    "Devuelve la posición del máximo elemento en un segmento de
    lista de elementos comparables.
    La lista no debe ser vacía.
    a y b son las posiciones inicial y final del segmento
    """

    pos_max = a
    for i in range(a + 1, b + 1):
        print(lista[i], lista[pos_max], i)
        if lista[i] > lista[pos_max]:

            pos_max = i
    return pos_max


l = [3, 2, -1, 5, 0, 2]
ord_seleccion(l)
