from raton import Raton
from teclado import Teclado
from monitor import Monitor


class Computadora:

    contador_compu = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_compu += 1
        self._id_producto = Computadora.contador_compu
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    def __str__(self):
        return f'\t\tID computadora: {self._id_producto}\n \
                 \n\t\tNombre: {self._nombre}\n   \
                 \n\t\tMonitor: {self._monitor}\n \
                 \n\t\tTeclado: {self._teclado}\n \
                 \n\t\tRaton: {self._raton}\n \
                 '


if __name__ == '__main__':  # es como una prueba
    obj_raton1 = Raton(marca='HP', tipo_entrada="USB")
    obj_raton2 = Raton(marca='Acer', tipo_entrada="Bluetooth")
    obj_teclado1 = Teclado(marca='Super teclado', tipo_entrada="USB")
    obj_teclado2 = Teclado(marca='ACME', tipo_entrada="Bluetooth")
    obj_monitor1 = Monitor(marca='HP', pantalla=15)
    obj_monitor2 = Monitor(marca='Acer', pantalla=14)

    obj_compu1 = Computadora(nombre='HP', monitor=obj_monitor1, teclado=obj_teclado1, raton=obj_raton1)
    obj_compu2 = Computadora(nombre='Acer super PC', monitor=obj_monitor2, teclado=obj_teclado2, raton=obj_raton2)
    print(obj_compu1)
    print(obj_compu2)
