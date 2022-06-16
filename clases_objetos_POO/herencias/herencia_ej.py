class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f'Nombre: {self.nombre}, Apellido: {self.apellido}'


class Empleado(Persona):
    def __init__(self, nombre, apellido, legajo):
        # super() nos permite acceder a los metodos de la clase padre
        super().__init__(nombre, apellido)
        self.legajo = legajo

    def __str__(self):
        return f'{super().__str__()}, Legajo: {self.legajo}'


empleado_obj = Empleado("Pepe", "ApellidoPepe", 2323)
print(empleado_obj.nombre)
print(empleado_obj.apellido)
print(empleado_obj.legajo)
