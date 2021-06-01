from dispositivo_de_entrada import DispositivoEntrada


class Teclado(DispositivoEntrada):

    contador_producto = 0

    def __init__(self, marca, tipo_entrada):
        Teclado.contador_producto += 1
        self._id_producto = Teclado.contador_producto
        super().__init__(marca, tipo_entrada)

    def __str__(self):
        return f'\tID Teclado: {self._id_producto} \
                 \n\t\t\t\tMarca: {self._marca} \
                 \n\t\t\t\tTipo de entrada: {self._tipo_entrada}\n'


if __name__ == '__main__':  # es como una prueba
    obj_teclado1 = Teclado(marca='Super teclado', tipo_entrada="USB")
    obj_teclado2 = Teclado(marca='ACME', tipo_entrada="Bluetooth")
    print(obj_teclado1)
    print(obj_teclado2)
