# Son tipos de datos abstractos
'''
Operaciones:
    - __init__: Inicializa una pila nueva, vacía
    - Apilar: Agregar un nuevo elemnto a la pila
    - Desapilar: Elimina el tope de la pila y lo devuelve.
    El elemnto que se devuelve es el último que se agrego
    - esta_vacia: Devuelve True o False segun la pila está vacía

    "Lo último que se apilo es lo primero que se usa"
'''


class Pila:
    """Representa una pila con operaciones de apilar, desapilar,
    y verificar si está vacía
    """

    def __init__(self):
        """Crea una pila vacía."""
        self.items = []

    def esta_vacia(self):
        """Devuelve True si la lista está vacía"""
        return len(self.items) == 0

    def apilar(self, x):
        """Agrega/apila el elemnto X al final de la lista"""
        self.items.append(x)

    def desapilar(self):
        """Devuelve el primer elemento/tope y lo elimina.
        Si la pila está vacía levanta una excepción"""
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        return self.items.pop()


# Ejemplos
# p = Pila()
# print(p.esta_vacia())
# p.apilar(1)
# print(p.esta_vacia())
# p.apilar(5)
# p.apilar("###")
# p.apilar("&&&")
# print(p.items)
# print(p.desapilar())
# q = Pila()
# q.desapilar()
