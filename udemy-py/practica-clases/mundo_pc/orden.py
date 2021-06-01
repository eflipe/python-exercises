class Orden:
    contador_orden = 0

    def __init__(self, computadoras):
        Orden.contador_orden += 1
        self._id_orden = Orden.contador_orden
        self._computadoras = computadoras

    def agregar_compus(self, computadora):
        self._computadoras.append(computadora)

    def __str__(self):
        compus_str = ''
        for compu in self._computadoras:
            compus_str += compu.__str__() + '----' + '\n'

        return f'''
            Orden de compra: {self._id_orden}
            Computadoras: \n {compus_str}
                '''
