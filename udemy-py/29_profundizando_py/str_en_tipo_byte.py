# los str de tipo bytes empiezan con b''
ejemplo_en_bytes = b'Hola mundo'
print(ejemplo_en_bytes)
print(ejemplo_en_bytes[0])
print(chr(ejemplo_en_bytes[0]))

# convertir de str a bytes

ejemplo_str = 'Hola mundo ñó;\''
print('Hola mundo')

bytes = ejemplo_str.encode('UTF-8')
print('Bytes ', bytes)

# convertir bytes a str
ejemplo_dos = bytes.decode('UTF-8')
print('ejemplo dos: ', ejemplo_dos)
