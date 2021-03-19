# concepto herencia multiple
from _45_herencia_multiple import FiguraGeometrica
from color import Color


# area del cuadrado
class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, alto, ancho, color):
        FiguraGeometrica.__init__(self, alto, ancho)
        Color.__init__(self, color)

    def area(self):
        return self.get_alto() * self.get_ancho()

    def __str__(self):
        return FiguraGeometrica.__str__(self) + ", Color: " + self.get_color()
