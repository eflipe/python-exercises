from clase_raton import Raton
from clase_teclado import Teclado
from clase_monitor import Monitor
from clase_computadora import Computadora
from clase_orden import Orden

obj_monitor = Monitor('Monitor sin marca', '10 pulgadas')
obj_teclado = Teclado("SuperMarca", "USB")
obj_raton = Raton("Marca Raton", "Entrada Raton")
obj_computadora = Computadora("SuperCompu", obj_monitor, obj_teclado, obj_raton)
# print(obj_computadora)
obj_monitor_1 = Monitor('Monitor sin marca 2', '2 pulgadas')
obj_teclado_1 = Teclado("SuperMarca 2", "USB")
obj_raton_1 = Raton("Marca Raton 2", "Entrada Raton")
obj_computadora_1 = Computadora("SuperCompu 2", obj_monitor_1, obj_teclado_1, obj_raton_1)
# print(obj_computadora_1)
obj_monitor_2 = Monitor('Monitor sin marca 3', '3 pulgadas')
obj_teclado_2 = Teclado("SuperMarca 3", "USB")
obj_raton_2 = Raton("Marca Raton 3", "Entrada Raton")
obj_computadora_2 = Computadora("SuperCompu 3", obj_monitor_2, obj_teclado_2, obj_raton_2)

computadora_list = [obj_computadora, obj_computadora_1]
obj_orden = Orden(computadora_list)
print(obj_orden)
print("Agregamos otra compu:")
obj_orden.agregar_computadoras(obj_computadora_2)
print(obj_orden)
print("Creamos otra orden:")
obj_orden = Orden([obj_computadora_2, obj_computadora])
print(obj_orden)
