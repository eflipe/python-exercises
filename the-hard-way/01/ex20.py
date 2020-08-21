from sys import argv

script, input_file = argv

current_file = open(input_file)


def print_all(f):
    print(f.read())


def rewind(f):
    f.seek(0)


def print_a_line(line_count, f):
    print(line_count, f.readline(), end='')


print("Todo el file: \n")
print_all(current_file)
print("Rewind")
rewind(current_file)
print('Mostrar 3 lineas\n')
current_line = 1
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)
print('\n')