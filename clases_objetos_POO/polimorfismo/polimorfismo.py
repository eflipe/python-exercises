# polimorfismo: multiples formas en tiempo de ejecucion
from class_empleado import Empleado
from class_gerente import Gerente


def imprimir_detalles(obj):
    # print(obj)
    print(type(obj))
    print(obj.mostrar_detalles())
    if isinstance(obj, Gerente):
        print('Si')
        print(obj.departamento)


obj_empleado = Empleado("Pepe", 5000)
imprimir_detalles(obj_empleado)

obj_gerente = Gerente("Karla", 6000, 'Sistemas')
imprimir_detalles(obj_gerente)
