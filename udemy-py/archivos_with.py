# with: manejo de contexto, regresa el archivo y lo cierra
# utiliza los metodos __enter__ y __exit__
from manejo_archivos.class_manejo_archivo import ManejoArchivos



# with open('prueba_2.txt', 'r', encoding='utf8') as archivo:
#     print(archivo.read())


with ManejoArchivos('C:\\Users\\Felipe\\Exercism\\python\\python-exercises\\prueba.txt') as file:
    print(file.read())
