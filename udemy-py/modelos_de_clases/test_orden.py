from producto import Producto
from orden_compra import OrdenDeCompra

producto_1 = Producto('Jarrón', 55.55)

print(producto_1)

producto_2 = Producto('Avión', 101.10)
producto_3 = Producto('Nave espacial', 111.11)

print(producto_2)

productos = [producto_1, producto_2]

orden_1 = OrdenDeCompra(productos)
print(orden_1.calcular_total())
productos.append(producto_3)
orden_2 = OrdenDeCompra(productos)
print(orden_2)
orden_3 = OrdenDeCompra(productos)
orden_3.agregar_producto(producto_1)
print(orden_3)
