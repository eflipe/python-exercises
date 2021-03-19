from cuadrado import Cuadrado
from rectangulo import Rectangulo

cuadrado = Cuadrado(4, 4, 'verde')

print(cuadrado.area())

print(cuadrado)

#method resolution order
print(Cuadrado.mro())

f2 = Rectangulo(10, 5, "Azul")

print("Rectangulo: ", f2)
print("Area del Rectangulo: ", f2.area())
