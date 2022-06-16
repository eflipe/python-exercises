# a partir de una clase se crean objetos
# atributos = caracteristicas del objetos
# metodos = comportamiento, acciones del objeto. Es igual a una funcion
class Persona:
    # clase llamada Persona
    # usamos el metodo __init__ para agregar atributos a la clase
    # y tambien para inicializarlos
    # puede recibir parametros, en este ejemplo son nombre y apellido
    # *args para pasar una tupla de valores, **kwargs para diccionarios

    def __init__(self, nombre, apellido, *args, **kwargs):
        # son atributos que estan relacionados a los objetos
        # son atributos de instancia
        self.nombre = nombre
        self.apellido = apellido
        self.args = args
        self.kwargs = kwargs

    def mostrar_detalle(self):
        return f'Persona: {self.nombre}, {self.apellido},  {self.args},  {self.kwargs}'







print(type(Persona))
# creamos instancias
#  instancia = creacion de objetos

objeto_persona = Persona('Pepe', 'Fulano', 3, 4, 4, m='manzana') # se llama al metodo __init__
print(objeto_persona)
#usamos directamente el objeto
print(objeto_persona.nombre)
print(objeto_persona.apellido)
print(objeto_persona.args)
print(objeto_persona.kwargs['m'])
print(objeto_persona.mostrar_detalle())

# tambien podemos instaciar asi (no es comun)
print("----")
print(Persona.mostrar_detalle(objeto_persona))
