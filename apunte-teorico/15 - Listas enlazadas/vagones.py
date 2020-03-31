class Nodo:
    def __init__(self, dato=None, prox=None):
        self.dato = dato
        self.prox = prox

    def __str__(self):
        return str(self.dato)


n3 = Nodo("Bananas")
n2 = Nodo("Peras", n3)
n1 = Nodo("Manzanas", n2)

print(str(n1))
print(n1)

def ver_lista(nodo):
    """Recorre los nodos a través de sus enlaces (.prox)
    mostrando su contenido"""
    while nodo is not None:
        print(nodo)
        nodo = nodo.prox


ver_lista(n1)
