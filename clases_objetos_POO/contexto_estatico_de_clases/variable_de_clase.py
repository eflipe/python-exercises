class MiClase:
    # VAriable de clase: estan afuera del init
    # se asocia con la clase en si misma y NO con ningun objeto
    # lo que está dentro de init son las varibles de instancias
    variable_clase = 'Valor de clase'

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia


# se asocia con la clase en si misma y NO con ningun objeto
# por eso esto funciona
print(MiClase.variable_clase)
# para acceder a la varible intancia
obj_miClase = MiClase("VAlor variable instancias")
print(obj_miClase.variable_instancia)
# accedemos a la variable de clase
print(obj_miClase.variable_clase)
