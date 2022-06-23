from figura_geo import FiguraGeometrica
from clase_color import Color


class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, ancho, alto, color):
        # hay que volver a pasarles self
        FiguraGeometrica.__init__(self, ancho, alto)
        Color.__init__(self, color)

    def calcular_area(self):
        return self.alto * self.ancho
