class Monitor:
    contador = 0

    def __init__(self, marca, tamanio):
        Monitor.contador += 1
        self._id_monitor = Monitor.contador
        self._marca = marca
        self._tamanio = tamanio

    def __str__(self):
        return f'ID: {self._id_monitor}, Marca: {self._marca}, Tamaño: {self._tamanio}'


if __name__ == '__main__':
    obj_monitor = Monitor('MarcaPepe', '14 pulgadas')
    print(obj_monitor)
    obj_monitor_2 = Monitor('Monitor sin marca', '10 pulgadas')
    print(obj_monitor_2)
