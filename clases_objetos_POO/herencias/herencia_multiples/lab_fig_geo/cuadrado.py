from figura_geometrica import FiguraGeometrica
from color import Color


class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def calcular_area(self):
        return self.alto * self.ancho

    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)} \
                 \n{Color.__str__(self)} \
                 \nArea: {self.calcular_area()}'
