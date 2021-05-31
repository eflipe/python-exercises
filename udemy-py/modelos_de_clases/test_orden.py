from producto import Producto
from orden_compra import OrdenDeCompra

producto_1 = Producto('Jarrón', 50.55)

print(producto_1)

producto_2 = Producto('Avión', 50.10)
producto_3 = Producto('Nave espacial', 50.11)

print(producto_2)

productos = [producto_1, producto_2]

orden_1 = OrdenDeCompra(productos)
print(orden_1.calcular_total())
print("Orden 1: ", orden_1)
orden_1.agregar_producto(producto_3)
print("Orden 1, con un producto más: ", orden_1)
productos.append(producto_3)
orden_2 = OrdenDeCompra(productos)
print(orden_2)

orden_3 = OrdenDeCompra(productos)
orden_3.agregar_producto(producto_1)
print(orden_3)
print("Total orden 1: ", orden_1.calcular_total())
print("Total orden 3: ", orden_3.calcular_total())
print("Total orden 2: ", orden_2.calcular_total())
