# División y conquista
def merge_sort(lista):
    """Ordena la lista mediante el método merge"""
    if len(lista) < 2:
        return lista

    medio = len(lista) // 2
    izq = merge_sort(lista[:medio])
    der = merge_sort(lista[medio:])
    return merge(izq, der)


def merge(lista1, lista2):
    """Intercala los elementos de lista1 y lista2 de forma ordenada."""

    i, j = 0, 0
    resultado = []

    while(i < len(lista1) and j < len(lista2)):
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1
    # Agregar lo que falta
    resultado += lista1[i:]
    resultado += lista2[j:]

    return resultado
