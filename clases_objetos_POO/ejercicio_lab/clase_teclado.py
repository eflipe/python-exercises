from clase_dispositivos_entrada import DispositivoEntrada


class Teclado(DispositivoEntrada):
    contador = 0

    def __init__(self, marca, tipo_entrada):
        Teclado.contador += 1
        self._id_teclado = Teclado.contador
        super().__init__(marca, tipo_entrada)

    def __str__(self):
        return f'ID: {self._id_teclado}, Marca: {self._marca}, Tipo: {self._tipo_entrada}'


if __name__ == '__main__':
    obj_teclado = Teclado("SuperMarca", "USB")
    print(obj_teclado)
    obj_teclado_2 = Teclado("OtraMarca", "Cable")
    print(obj_teclado_2)
