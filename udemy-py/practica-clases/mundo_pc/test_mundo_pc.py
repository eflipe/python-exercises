from raton import Raton
from teclado import Teclado
from monitor import Monitor
from computadora import Computadora
from orden import Orden

obj_raton1 = Raton(marca='HP', tipo_entrada="USB")
obj_raton2 = Raton(marca='Acer', tipo_entrada="Bluetooth")
obj_teclado1 = Teclado(marca='Super teclado', tipo_entrada="USB")
obj_teclado2 = Teclado(marca='ACME', tipo_entrada="Bluetooth")
obj_monitor1 = Monitor(marca='HP', pantalla=15)
obj_monitor2 = Monitor(marca='Acer', pantalla=14)

obj_compu1 = Computadora(nombre='HP', monitor=obj_monitor1, teclado=obj_teclado1, raton=obj_raton1)
obj_compu2 = Computadora(nombre='Acer super PC', monitor=obj_monitor2, teclado=obj_teclado2, raton=obj_raton2)

compus_list = [obj_compu1, obj_compu2]
orden_1 = Orden(computadoras=compus_list)
orden_2 = Orden(computadoras=compus_list)
orden_3 = Orden(computadoras=compus_list)
print(orden_1)
orden_3.agregar_compus(obj_compu1)
print(orden_3)
