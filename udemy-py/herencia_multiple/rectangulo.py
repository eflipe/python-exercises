# concepto herencia multiple
from _45_herencia_multiple import FiguraGeometrica
from color import Color


class Rectangulo(FiguraGeometrica, Color):
    def __init__(self,ancho,alto,color):
        FiguraGeometrica.__init__(self,ancho,alto)
        Color.__init__(self,color)

    def area(self):
        return self.get_ancho() * self.get_alto()

    def __str__(self):
        return FiguraGeometrica.__str__(self) +", Color: "+ self.get_color()
