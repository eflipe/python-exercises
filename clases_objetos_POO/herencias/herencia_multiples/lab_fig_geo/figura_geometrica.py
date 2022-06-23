class FiguraGeometrica:
    def __init__(self, ancho, alto):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            self._ancho = 0
            print(f'Error, el valor ingresado es: {ancho}')
        if self._validar_valor(alto):
            self._alto = alto
        else:
            self._alto = 0
            print(f'Error, el valor ingresado es: {alto}')

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            print(f'Error, el valor ingresado es: {ancho}')

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        if self._validar_valor(alto):
            self._alto = alto
        else:
            print(f'Error, el valor ingresado es: {alto}')

    def __str__(self):
        return f'Alto: {self._alto}, Ancho: {self._ancho}'

    def _validar_valor(self, valor):
        return True if 0 < valor < 10 else False

if __name__ == '__main__':
    obj_fig_geo = FiguraGeometrica(8, 9)
    print(obj_fig_geo)
    print("Cambiamos el ancho")
    obj_fig_geo.ancho = 10
    print(obj_fig_geo)
    print("Cambiamos el alto")
    obj_fig_geo.alto = 10
    print(obj_fig_geo)
