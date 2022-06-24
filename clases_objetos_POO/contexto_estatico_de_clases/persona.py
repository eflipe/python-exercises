class Persona:
    contador_persona = 0

    @classmethod
    def next_value(cls):
        cls.contador_persona += 1
        return cls.contador_persona

    def __init__(self, nombre, apellido=''):
        self.id_persona = Persona.next_value()
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f'Nombre: {self.nombre}, Apellido: {self.apellido}, ID: {self.id_persona} Contador: {Persona.contador_persona}'


if __name__ == '__main__':
    obj_persona = Persona('Juan', 'Juanchinosky')
    print(obj_persona)
    obj_persona_2 = Persona('Jacinta')
    print(obj_persona_2)
