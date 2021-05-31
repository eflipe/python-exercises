class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    # metodo sobreescrito de la clase padre object
    def __add__(self, otro):  # otro: es el otro objeto que se pasa como parametro
        return self.__nombre + " " + otro.__nombre

    def __sub__(self, otro):
        return self.__edad - otro.__edad


p1 = Persona("Juan", 55)
p2 = Persona("Karla", 40)

# una nueva forma de trabajar al operador +
print(p1 + p2)

print(p1 - p2)
