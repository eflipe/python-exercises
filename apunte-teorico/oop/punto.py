class Punto:
    """Representación de un punto en el plano # -*- coding: utf-8 -*-
    coordenadas cartesianas (x, y)"""

    def __init__(self, x, y):
        """Constructor de Punto.
        x e y deben ser numéricos"""
        self.x = validar_numero(x)
        self.y = validar_numero(y)

    def distancia(self, otro):
        """Devuelve la distancia entre dos objetos Punto"""
        dx = self.x - otro.x
        dy = self.y - otro.y
        return (dx * dx + dy * dy) ** 0.5

    def __str__(self):
        """Devuelve la representación del punto como una
        cadena de texto"""
        return f"({self.x},{self.y})"

    def desplazar(self, dx, dy):
        self.x += dx
        self.y += dy
        return f"Punto ({self.x}, {self.y})"

    def __eq__(self, otro):
        """Comprueba si dos puntos son iguales"""
        return self.x == otro.x and self.y == otro.y

    def __repr__(self):
        """Devuelve la representación formal del Punto como
        cadena de texto."""
        return f"Punto({self.x}, {self.y})"


def validar_numero(valor):
    """Si el valor es númerico, lo devuelve.
    En caso contario muestra Error"""
    if not isinstance(valor, (int, float, complex)):
        raise TypeError(f"{valor} no es un valor numérico.")
    return valor


p = Punto(5, 7)
print(type(p))
print(str(p))
print(repr(p))
# p2 = Punto("A", 5)
p = Punto(10, 15)
q = Punto(5, 10)
print(p.distancia(q))

x = Punto(5, 7)
x2 = Punto(10, 15)
z = Punto(2, 3)
print(x.distancia(z))
print(x.desplazar(5, 7))
print(p == x2)
print(x != p)
