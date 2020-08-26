i = 0
numbers = []

while i < 6:
    print(f'Arranca con {i}')
    numbers.append(i)

    i += 1
    print('Num acumulados', numbers)
    print(f'i al final: {i}')

print('Los num:')
for num in numbers:
    print(num)