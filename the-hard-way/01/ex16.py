from sys import argv

script, filename = argv

print(f'Vamos a robar {filename}')
input('Enter para seguir')
print('Abriendo el archivo')
target = open(filename, 'w')
print('Truncating...')
target.truncate()
print('Nuevas lineas: ')
line1 = input('1: ')
line2 = input('2: ')
line3 = input('3: ')
print('Escribiendo...')
target.write(f'{line1}\n{line2}\n\t*{line3}\n')

target.close()