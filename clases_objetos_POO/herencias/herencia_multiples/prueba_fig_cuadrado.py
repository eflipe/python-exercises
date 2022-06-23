from clase_cuadrado import Cuadrado

obj_cuadrado = Cuadrado(5, 5, 'rojo')
print(obj_cuadrado.color)
print(obj_cuadrado.ancho)
print(obj_cuadrado.alto)
print(obj_cuadrado.calcular_area())

# mro: sivre para ver que clases se ejecutan (y su orden)
print(Cuadrado.mro())
