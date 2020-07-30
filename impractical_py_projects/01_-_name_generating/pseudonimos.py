"""Generate funny names by randomly combining names from 2 separate
lists."""
import sys
import random
import io


print("Programita que genera nombres graciosos.\n")
print("#Ponele\n\n")

FILENAME = 'nombres.txt'

with io.open(FILENAME, 'r', encoding='utf8') as f:
    nombres = f.readlines()


listaNombres = []
nombre, apellido = [], []
for n in range(len(nombres)):
    listaNombres.append(nombres[n].strip('\n').split(' '))
    nombre.append(listaNombres[n][0])
    apellido.append(listaNombres[n][1])

while True:
    first_name = random.choice(nombre)
    last_name = random.choice(apellido)

    print("\n\n")
    print("{} {}".format(first_name, last_name), file=sys.stderr)
    print("\n\n")

    try_again = input("\n\n Otro intento? (n)")
    if try_again.lower() == "n":
        break

input("\nPress Enter to exit.")
