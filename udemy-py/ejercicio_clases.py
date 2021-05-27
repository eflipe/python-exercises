'''
Definir una clase padre llamada Vehiculo y dos clases hijas llamadas Coche y
Bicicleta, las cuales heredan de la clase Padre Vehiculo
'''

# clase Padre


class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f'Color: {self.color}, Ruedas: {self.ruedas}'


class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return f'{super().__str__()}, Velocidad: {self.velocidad}'

obj_1 = Vehiculo("Rojo", 4)
print(obj_1)

obj_2 = Coche("Azul", 4, 200)
print(obj_2)
