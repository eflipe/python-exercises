from clase_producto import Producto
from clase_orden import Orden

obj_producto = Producto('Auto', 5000)
print(obj_producto)
obj_producto_2 = Producto('Nave espacial', 11000)
obj_producto_3 = Producto('Estrella', 11000)
print(obj_producto_3)
lista_productos = [obj_producto, obj_producto_2, obj_producto_3]
obj_orden = Orden(lista_productos)
print(obj_orden)
obj_orden_2 = Orden(lista_productos)
print(obj_orden_2)
print(f'total orden 2: {obj_orden_2.calcular_total()}')
print("Agregamos un producto")
obj_orden_2.agregar_producto(obj_producto)
print(obj_orden_2)
print(f'total orden 2: {obj_orden_2.calcular_total()}')
