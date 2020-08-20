from sys import argv

script, filename = argv

txt = open(filename)

print(f'Este archivo abrirás: {filename}')
print(txt.read())

print(f'Escribilo otra vez: ')
file_again = input(' >')

txt_again = open(file_again)

print(txt_again.read())