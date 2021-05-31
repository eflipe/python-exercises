from producto import Producto


class OrdenDeCompra():
    contador_ordenes = 0

    def __init__(self, productos):
        OrdenDeCompra.contador_ordenes += 1
        self.__id_orden = OrdenDeCompra.contador_ordenes
        self.__productos = list(productos)

    def agregar_producto(self, producto):
        self.__productos.append(producto)
        return producto

    def calcular_total(self):
        total = 0
        for producto in self.__productos:
            total += producto.get_precio

        return total

    def __str__(self):
        productos_str = ""
        for producto in self.__productos:
            productos_str += producto.__str__() + " / "

        return f'ID ORDEN: {self.__id_orden} , Productos {productos_str}'


if __name__ == '__main__':
    producto1 = Producto('Botas', 100)
    producto2 = Producto('Camisa', 100)
    lista_productos = [producto1, producto2]

    orden = OrdenDeCompra(lista_productos)
    print(orden.agregar_producto(producto1))
    print(orden.agregar_producto(producto1))
    print(orden.calcular_total())
    # print(orden.calcular_total())
    print(orden)
    orden_2 = OrdenDeCompra(lista_productos)
    print(orden_2)
    print(orden_2.calcular_total())
