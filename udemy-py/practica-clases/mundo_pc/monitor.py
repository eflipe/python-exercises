class Monitor:

    contador_monitor = 0

    def __init__(self, marca, pantalla):
        Monitor.contador_monitor += 1
        self._id_producto = Monitor.contador_monitor
        self._marca = marca
        self._pantalla = pantalla

    def __str__(self):
        return f'\tID monitor: {self._id_producto} \
                 \n\t\t\t\tMarca: {self._marca} \
                 \n\t\t\t\tTamaño pantalla: {self._pantalla}\n'


if __name__ == '__main__':  # es como una prueba
    obj_monitor1 = Monitor(marca='HP', pantalla=15)
    obj_monitor2 = Monitor(marca='Acer', pantalla=14)
    print(obj_monitor1)
    print(obj_monitor2)
