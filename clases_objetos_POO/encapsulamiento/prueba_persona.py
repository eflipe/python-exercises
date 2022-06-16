from persona_obj import Persona

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

print("Eliminando...".center(30, '*'))
del persona_obj
