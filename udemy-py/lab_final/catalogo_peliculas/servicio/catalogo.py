import os


class CatalogoPeliculas:

    ruta_archivo = "peliculas.txt"

    @classmethod
    def agregar_pelicula(cls, pelicula):  # cls: contexto de clase
        with open(cls.ruta_archivo, 'a', encoding='utf8') as file:
            file.write(f'{pelicula.nombre}\n')

    @classmethod
    def listar_peliculas(cls):
        with open(cls.ruta_archivo, 'r', encoding='utf8') as file:
            print('Catalogo'.center(50, '-'))
            print(file.read())

    @classmethod
    def eliminar_archivo(cls):
        os.remove(cls.ruta_archivo)
        print(f"Archivo eliminado: {cls.ruta_archivo}")
