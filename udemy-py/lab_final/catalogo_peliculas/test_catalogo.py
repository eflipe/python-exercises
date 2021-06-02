from dominio.pelicula import Pelicula
from servicio.catalogo import CatalogoPeliculas

opcion = None

while opcion != 4:
    try:
        print("Menú de opciones")
        print("1) Agregar film")
        print("2) Listar films")
        print("3) Eliminar archivo")
        print("4) Salir")
        opcion = int(input("Selecciona entre 1-4: "))

        if opcion == 1:
            nombre_film = input("Ingresar nombre peli")
            pelicula = Pelicula(nombre_film)
            CatalogoPeliculas.agregar_pelicula(pelicula)

        elif opcion == 2:
            print("Lista de films: ")
            CatalogoPeliculas.listar_peliculas()

        elif opcion == 3:
            CatalogoPeliculas.eliminar_archivo()


    except Exception as e:
        print("Error del tipo: ", e)
        print("Recuerde ingresar un valor entre 1-4")
        opcion = None
else:
    print("Programa finalizado")
