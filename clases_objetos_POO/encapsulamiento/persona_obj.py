class Persona:
    # el guion bajo nos dice que no debemos acceder al atributo
    # solamente se puede acceder/modificar mediante metodos set(modificar)/get(obtener)
    def __init__(self, nombre, apellido):
        self._nombre = nombre
        self._apellido = apellido

    # decodador property: modifica el comportamiento de nuestro metodo
    # con @property podemos acceder a nuestro metodo como si fuese un atributo
    @property
    def get_nombre(self):
        return self._nombre

    @get_nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    def mostrar_detalle(self):
        return f'Persona, nombre y apellido: {self._nombre}, {self._apellido}'

    # metodo destructor
    def __del__(self):
        print("Objeto eliminado", self._nombre)


if __name__ == '__main__':
    persona_obj = Persona("Pepe", "Fulano")
    print(persona_obj.get_nombre)
    print("Cambiamos nombre: ")
    persona_obj.nombre = "Mengano"
    print(persona_obj.get_nombre)
    print("Apellido: ", persona_obj.apellido)
    print("Cambiamos apellido: ")
    persona_obj.apellido = "Nuevo apellido"
    print("Apellido nuevo: ", persona_obj.apellido)
    print(persona_obj.mostrar_detalle())
