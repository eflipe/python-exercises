class ClaseRectangulo:
    '''Calcula el area de un rectangulo'''

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura


input_base = int(input("Base: "))
input_altura = int(input("Altura: "))

obj_rectangulo = ClaseRectangulo(input_base, input_altura)
print(f'Area: {obj_rectangulo.calcular_area()}')
