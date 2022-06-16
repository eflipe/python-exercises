class ClaseCubo:
    # *args para pasar una tupla de valores, **kwargs para diccionarios
    def __init__(self, ancho, alto, profundo):
        self.ancho = ancho
        self.alto = alto
        self.profundo = profundo

    def calcular_volumen(self):
        return self.ancho * self.alto * self.profundo


ancho = int(input("Ancho: "))
alto = int(input("Alto: "))
profundo = int(input("Profundo: "))

cubo_obj = ClaseCubo(ancho, alto, profundo)
print(f'Volumen cubo:{cubo_obj.calcular_volumen()}')
