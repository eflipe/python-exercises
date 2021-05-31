class Producto:
    contador_productos = 0

    def __init__(self, nombre, precio):
        Producto.contador_productos += 1
        self.__id_producto = Producto.contador_productos
        self.__nombre = nombre
        self.__precio = precio

    @property
    def get_precio(self):
        return self.__precio

    def __str__(self):
        return f'\tID producto: {self.__id_producto}\t \
                Nombre: {self.__nombre}\t \
                Precio: {self.__precio}'


if __name__ == '__main__':
    producto1 = Producto('Botas', 555)
    print(producto1)
