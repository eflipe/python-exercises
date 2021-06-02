archivo = open('C:\\Users\\Felipe\\Exercism\\python\\python-exercises\\prueba.txt', 'r', encoding='utf8')
# print(archivo.read(5)) # leemos solo 5 chars
# print(archivo.read(6))
# print(archivo.readline())
# print(archivo.readline())

# leer lineas
# for linea in archivo:
#     print(linea)

# readlineS : devuelve una lista
# print(archivo.readlines())
# print(archivo.readlines()[0])

# agregamos info, NO la sobreescribe, la anexa
archivo2 = open('copia.txt', 'a', encoding="utf8")
archivo2.write(archivo.read()) # realizamos un copia

archivo.close()
archivo2.close()
