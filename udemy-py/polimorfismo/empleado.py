class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

    def __str__(self):
        return "Nombre: " + self.nombre + ", sueldo: " + str(self.sueldo)

    def mostrar_detalles(self):
        return self.__str__()
