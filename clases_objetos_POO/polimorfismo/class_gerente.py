from class_empleado import Empleado


class Gerente(Empleado):
    def __init__(self, nombre, sueldo, departamento):
        super().__init__(nombre, sueldo)
        self.departamento = departamento

    def __str__(self):
        mensaje = f'{super().__str__()}, Departamento: {self.departamento}'
        return mensaje
