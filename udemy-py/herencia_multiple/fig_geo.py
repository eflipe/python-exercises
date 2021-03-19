from cuadrado import Cuadrado
from rectangulo import Rectangulo
from _45_herencia_multiple import FiguraGeometrica

cuadrado = Cuadrado(4, 4, 'verde')

print(cuadrado.area())

print(cuadrado)

#method resolution order
print(Cuadrado.mro())

f2 = Rectangulo(10, 5, "Azul")

print("Rectangulo: ", f2)
print("Area del Rectangulo: ", f2.area())

# no es posible crear objetos de una clase abstracta
# f3 = FiguraGeometrica()
