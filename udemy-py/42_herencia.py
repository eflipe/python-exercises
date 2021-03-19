class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Nombre: {self.nombre}, Edad: {self.edad}'



class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def __str__(self):
        persona_str = super().__str__()
        return f'{persona_str}, Sueldo: {self.sueldo}'

# objeto clase Padre

persona_padre = Persona('Pepe', 33)
print(persona_padre)

empleado = Empleado('Esteban', 77, 70777)
print(empleado)
