class Persona:
    contador_personas = 0  # variable de clase: se comparte para todos los obejtos de tipo contador_personas

    @classmethod
    def funcion_contador_personas(cls):
        cls.contador_personas += 1
        return cls.contador_personas

    def __init__(self, nombre, edad):
        self.id_persona = Persona.funcion_contador_personas()
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona: \n ID: {self.id_persona} \n Nombre: {self.nombre}, Edad: {self.edad}'


obj_1 = Persona("Pepe", 84)
print(obj_1)

obj_2 = Persona("Elena", 65)
print(obj_2)

print('Valor clase:', Persona.contador_personas)
print("Incremetandos.", Persona.funcion_contador_personas())

obj_3 = Persona("Fulano", 44)
print(obj_3)
