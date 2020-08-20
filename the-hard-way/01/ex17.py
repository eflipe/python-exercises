from sys import argv
from os.path import exists

script_name, from_file, to_file = argv

print(f'Copiando from {from_file} to {to_file}')
in_file = open(from_file)
indata = in_file.read()

print(f'Usamos len(): {len(indata)} bytes')
print(f' Existe el to_file? {exists(to_file)}')
input()

out_file = open(to_file, 'w')
out_file.write(indata)

out_file.close()
in_file.close()