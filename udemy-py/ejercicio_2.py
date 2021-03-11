"""
Se solicita incluir la siguiente información acerca de un libro:

titulo

autor

Debes imprimir la información en el siguiente formato:

Proporciona el titulo:
Proporciona el autor:
<titulo> fue escrito por <autor>
"""

titulo = input('Titulo: ')
autor = input('Autor: ')

print("Proporciona el titulo:", titulo)
print("Proporciona el autor:", autor)

print(titulo + ' fue escrito por ' + autor)
