from obj_vehiculo import Vehiculo


class Auto(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return f'{super().__str__()}, Velocidad: {self.velocidad}'


if __name__ == '__main__':
    obj_auto = Auto('Azul', 4, 120)
    print(obj_auto)
