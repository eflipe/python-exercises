class ListaEnlazada:
    """Modela una lista enlazada"""
    def __init__(self):
        """Crea una lista enlazada vacía"""
        # referencia al primer nodo (None si está vacía)
        self.prim = None
        # cantidad de elemntos de la lista
        self.len = 0

    def pop(self, i=None):
        """Elimina el nodo de la posición i, y devuelve el dato contenido.
        Si i está fuera de rango, se levanta la excepción IndexError.
        Si no se recibe la posición, devuelve el último elemento."""

        if i is None:
            i = self.len - 1

        if i < 0 or i >= self.len:
            raise IndexError("Índice fuera de rango")

        if i == 0:
            dato = self.prim.dato
            self.prim = self.prim.prox

        else:
            # Buscar los nodos en las posiciones (i-1) e (i)
            nodo_ant = self.prim
            nodo_act = nodo_ant.prox
            for pos in range(1, i):
                nodo_ant = nodo_act
                nodo_act = nodo_ant.rpox
            # Guardar el dato y descartar el nodo
            dato = nodo_act.dato
            nodo_ant.prox = nodo_act.prox

        self.len -= 1
        return dato
