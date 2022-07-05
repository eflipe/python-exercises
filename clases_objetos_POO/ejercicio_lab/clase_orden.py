class Orden:
    contador = 0
    # recibimos un listado de computadoras(Computadoras)

    def __init__(self, computadoras):
        Orden.contador += 1
        self._id_orden = Orden.contador
        self._computadoras = computadoras

    def agregar_computadoras(self, computadora):
        self._computadoras.append(computadora)

    def __str__(self):
        computadoras_str = ''
        for computadora in self._computadoras:
            computadoras_str += computadora.__str__()

        return f'''
        Orden ID: {self._id_orden}
        Computadoras: {computadoras_str}
        '''
