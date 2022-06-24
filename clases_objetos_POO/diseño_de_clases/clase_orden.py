from clase_producto import Producto

class Orden:
    contador_orden = 0

    @classmethod
    def next_value(cls):
        cls.contador_orden += 1
        return cls.contador_orden

    def __init__(self, lista_productos):
        self._id_orden = Orden.next_value()
        self._lista_productos = list(lista_productos)

    def agregar_producto(self, producto):
        self._lista_productos.append(producto)

    def calcular_total(self):
        total = 0

        for producto in self._lista_productos:
            total += producto.precio

        return total

    def __str__(self):
        productos_str = ''
        for producto in self._lista_productos:
            productos_str += producto.__str__() + '|'
        return f'Orden: {self._id_orden}, \nProductos: {productos_str}'


if __name__ == '__main__':
    obj_producto = Producto('Auto', 5000)
    print(obj_producto)
    obj_producto_2 = Producto('Nave espacial', 11000)
    print(obj_producto_2)
    lista_productos = [obj_producto, obj_producto_2]
    obj_orden = Orden(lista_productos)
    print(obj_orden)
    obj_orden_2 = Orden(lista_productos)
    print(obj_orden_2)
