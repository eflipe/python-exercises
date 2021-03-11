'''
Solicitar al usuario dos valores:

numero1 (int)

numero2 (int)

Se debe imprimir el mayor de los dos números (la salida debe ser identica a la que sigue):

Proporciona el numero1:
Proporciona el numero2:
El numero mayor es:<numeroMayor>

'''
numero1 = int(input('Ingrese un numero:'))
numero2 = int(input('Ingrese otro numero:'))
print("Proporciona el numero1:", numero1)
print("Proporciona el numero2:", numero2)

if numero1 > numero2:
    print("El numero mayor es:", numero1)
else:
    print("El numero mayor es:", numero2)
