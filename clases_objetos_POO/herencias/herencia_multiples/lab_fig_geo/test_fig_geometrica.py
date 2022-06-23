from cuadrado import Cuadrado
from rectangulo import Rectangulo

print('creacion Cuadrado:'.center(50, '*'))
obj_cuadrado = Cuadrado(lado=5, color='azul')
obj_cuadrado.alto = 6
print(obj_cuadrado)
print('creacion rectangulo:'.center(50, '-'))
obj_rectangulo = Rectangulo(ancho=10, alto=2, color='verde')
print(obj_rectangulo)
