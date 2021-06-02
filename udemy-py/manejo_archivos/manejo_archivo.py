# bloque try-exception para capturar la excepcion
try:
    archivo = open('prueba.txt', 'w', encoding='utf8')  # si el archivo no existe, entonces lo crea.
    archivo.write('Algo que por siempre recordemos.\n')
    archivo.write('Fin sin fin')
except Exception as e:
    print(e)
finally:
    archivo.close()
