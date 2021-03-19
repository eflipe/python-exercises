class MiClase:
    variable_clase = "Variable de claseee"

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia


print(MiClase.variable_clase)
# no funciona porque no se creo un objeto
obj1 = MiClase("Varibale instancia desde objeto")
MiClase.variable_instancia = "Modificando var instancia desde clase"
# esta variable pertence a la clase
print(MiClase.variable_instancia)
# esta clase pertenec al objeto
print(obj1.variable_instancia)

print(obj1.variable_clase)
print()
