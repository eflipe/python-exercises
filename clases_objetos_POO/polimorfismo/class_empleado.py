class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

    def __str__(self):
        mensaje = f'Nombre: {self.nombre}, Salario: {self.sueldo}'
        return mensaje

    def mostrar_detalles(self):
        return self.__str__()
