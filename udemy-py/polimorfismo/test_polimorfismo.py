from empleado import Empleado
from gerente import Gerente


def imprimir_detalles(objeto):
    print(objeto)
    print(objeto.nombre)
    if isinstance(objeto, Gerente):
        print(objeto.departamento)        
    print(type(objeto), end='\n\n')



empleado_1 = Empleado("Pepe", 1000)
imprimir_detalles(empleado_1)

# poliformismo
empleado_1 = Gerente("Oscar", 2000.00, "Sistemas")
imprimir_detalles(empleado_1)
