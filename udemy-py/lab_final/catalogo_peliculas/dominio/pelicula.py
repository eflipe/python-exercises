class Pelicula:
    def __init__(self, nombre):
        self._nombre = nombre

    def __str__(self):
        return f'Nombre del film: {self._nombre}'

    @property
    def get_nombre(self):
        return self._nombre

    @get_nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
