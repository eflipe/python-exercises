class Hotel:
    """Representa un hotel:
    Atributos: nombre, ubicacion, puntaje y precio"""

    def __init__(self, nombre, ubicacion, puntaje, precio):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.puntaje = puntaje
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} de {self.ubicacion} - Puntaje {self.puntaje} - Precio {self.precio} $"

    def ratio(self):
        """Calcula la relación precio-producto"""
        return ((self.puntaje ** 2) * 10) / self.precio

    def __lt__(self, otro):
        """Compara dos hoteles según sus ratios."""
        return self.ratio() < otro.ratio()


h = Hotel("The best", "Pehuajo", 3.2, 20)
print(h)
print(h.ratio())
h2 = Hotel("El 2do mejor", "Mendoza", 3, 30)
print(h2.ratio())
h3 = Hotel("Otro hotel", "Mendoza", 5, 30)
print(h3.ratio())
print(h < h2)
print(h > h2)

lista = [h, h2, h3]
lista.sort() # compara los ratios
print(lista)
for h in lista:
    print(h)
