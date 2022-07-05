from clase_raton import Raton
from clase_teclado import Teclado
from clase_monitor import Monitor

class Computadora:
    contador_compu = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_compu += 1
        self._id_computadora = Computadora.contador_compu
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    def __str__(self):
        return f'''
        Nombre: {self._nombre}, ID: {self._id_computadora}
        Monitor: {self._monitor}
        Teclado: {self._teclado}
        Raton: {self._raton}
        '''


if __name__ == '__main__':
    obj_monitor_2 = Monitor('Monitor sin marca', '10 pulgadas')
    obj_teclado = Teclado("SuperMarca", "USB")
    obj_raton = Raton("Marca Raton", "Entrada Raton")
    obj_computadora = Computadora("SuperCompu", obj_monitor_2, obj_teclado, obj_raton)
    print(obj_computadora)
