print("""
Opciòn 1 o 2:
""")

opcion = input('>')

if opcion == "1":
    print('Cuidado!')
    print('1.')
    print('2.')

    opcion_2 = input('>')

    if opcion_2 == "1":
        print('Zafaste')

    elif opcion_2 == "2":
        print('Noooo')

    else:
        print('Usate la opciòn {opcion_2}')

elif opcion == '2':
    print("Màs opciones!!!")
    print("1, 2 o 3")

    opcion_3 = input('> ')

    if opcion_3 == "1" or opcion_3 == "2":
        print('Yep')
    else:
        print('Ouch')

else:
    print("Ninguna opción seleccionada")