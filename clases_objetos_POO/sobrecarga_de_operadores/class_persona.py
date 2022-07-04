class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __add__(self, other):
        nombre = len(self.nombre)
        otro_nombre = len(other.nombre)
        return nombre + otro_nombre

    def __sub__(self, other):
        return self.edad - other.edad


if __name__ == '__main__':
    obj_1 = Persona("cinco", 11)
    obj_2 = Persona("seis", 10)
    suma_objs = obj_1 + obj_2
    sub_objs = obj_1 - obj_2
    print(sub_objs)
