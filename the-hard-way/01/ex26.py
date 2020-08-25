import sys

print('Edad?', end=' ')
age = input()
print("Altura?", end=' ')
height = input()
print("Peso?", end=' ')
weight = input()

print(f"Edad: {age}, Altura: {height}, Peso: {weight}")

script, filename = sys.argv

txt = open(filename)
print(f"Este es el nombre: {filename}")
print(txt.read())

print("Escriba otra el nombre")
file_again = input(">")

txt_again = open(file_again)


def txt_again_read(file):
    return file.read()


print(txt_again_read(txt_again))
