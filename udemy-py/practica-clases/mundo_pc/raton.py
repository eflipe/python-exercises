from dispositivo_de_entrada import DispositivoEntrada


class Raton(DispositivoEntrada):

    contador_producto = 0

    def __init__(self, marca, tipo_entrada):
        Raton.contador_producto += 1
        self._id_producto = Raton.contador_producto
        super().__init__(marca, tipo_entrada)

    def __str__(self):
        return f'\tID raton: {self._id_producto} \
                 \n\t\t\t\tMarca: {self._marca} \
                 \n\t\t\t\tTipo de entrada: {self._tipo_entrada}\n'


if __name__ == '__main__':  # es como una prueba
    obj_raton1 = Raton(marca='HP', tipo_entrada="USB")
    obj_raton2 = Raton(marca='Acer', tipo_entrada="Bluetooth")
    print(obj_raton1)
    print(obj_raton2)
