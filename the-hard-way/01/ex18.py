def print_two(*args):
    arg1, arg2 = args
    print(f'arg1: {arg1}, arg2: {arg2}')

# otra

def print_two_again(arg1, arg2):
    print(f'arg1: {arg1}, arg2: {arg2}')


def print_nada():
    print('Nada')


def print_for(*args):
    for arg in args:
        print(arg)


print_two('Pepe', 'Pepe_2')
print_two_again('Pepe_1', 'Pepe_3')
print_for('Pepe_11', 'Pepe_11', 'Pepe_11', 'Pepe_11', 'Pepe_11')