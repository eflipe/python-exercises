from obj_vehiculo import Vehiculo


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        # super() nos permite acceder a los metodos de la clase padre
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return f'{super().__str__()}, Tipo de bici: {self.tipo}'


if __name__ == '__main__':
    obj_bici = Bicicleta('rojo', 2, 'montaña')
    print(obj_bici)
