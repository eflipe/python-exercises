from clase_dispositivos_entrada import DispositivoEntrada


class Raton(DispositivoEntrada):
    contador_raton = 0

    def __init__(self, marca, tipo_entrada):
        Raton.contador_raton += 1
        self._id_raton = Raton.contador_raton
        super().__init__(marca, tipo_entrada)

    def __str__(self):
        return f'ID: {self._id_raton}, Marca: {self._marca}, Tipo entrada: {self._tipo_entrada}'


if __name__ == '__main__':
    obj_raton = Raton("Marca Raton", "Entrada Raton")
    print(obj_raton)
    obj_raton_2 = Raton("HP", "USB")
    print(obj_raton_2)
