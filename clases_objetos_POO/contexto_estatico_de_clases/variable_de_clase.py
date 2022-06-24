class MiClase:
    # VAriable de clase: estan afuera del init
    # se asocia con la clase en si misma y NO con ningun objeto
    # lo que está dentro de init son las varibles de instancias
    variable_clase = 'Valor de clase'
    variable_metodo_clase = "probando metodo de clase"

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

    # se asocia con la clase en si misma y no con los objetos
    # no puede acceder a las variables de instancia self
    @staticmethod
    def metodo_estatico():
        print(MiClase.variable_clase)

    # metodos de clase: si resive un contexto de clase (cls)
    @classmethod
    def metodo_clase(cls):
        print(cls.variable_metodo_clase)

    def metodo_instancia(self):
        self.metodo_estatico()
        self.metodo_clase()
        print(self.variable_clase)
        print(self.variable_instancia)


# se asocia con la clase en si misma y NO con ningun objeto
# por eso esto funciona
print(MiClase.variable_clase)
MiClase.metodo_estatico()
MiClase.metodo_clase()
# para acceder a la varible intancia
obj_miClase = MiClase("VAlor variable instancias")
print(obj_miClase.variable_instancia)
# accedemos a la variable de clase
print(obj_miClase.variable_clase)
obj_miClase.metodo_instancia()
