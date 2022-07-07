persona = ("Nombre 1", 'Apellido 1', 5000.00)
msj = 'Hola %s, %s. El numero es %.2f' % persona
print(msj)

ej_dict = {
    'nombre': 'Ivan',
    'edad': 35,
    'sueldo': 8000.00
}

msj = "Nombre: {persona[nombre]} Edad: {persona[edad]}, Sueldo: {persona[sueldo]:.2f}".format(persona=ej_dict)
print(msj)
