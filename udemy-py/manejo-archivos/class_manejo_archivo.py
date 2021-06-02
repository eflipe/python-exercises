# context manager: utiliza métodos __enter__ y __exit__


class ManejoArchivos:
    def __init__(self, nombre):
        self.nombre = nombre

    def __enter__(self):
        print("Obteniendo el recurso".center(50, '+'))
        self.nombre = open(self.nombre, 'r', encoding='utf8')
        return self.nombre

    def __exit__(self, tipo_excepcion, valor_exception, traza_error):  # son las firmas del método, podemos NO usarlas
        print("Cerramos el recurso".center(50, '+'))
        if self.nombre:
            self.nombre.close()
