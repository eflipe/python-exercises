resultado = None
try:
    a = int(input("Primer numero: "))
    b = int(input("Segundo numero: "))
    resultado = a / b

except ZeroDivisionError as err:
    print(f'Error division por zero: {err}, {type(err)}')

except TypeError as err:
    print(f'Error type error: {err}')

except Exception as err:
    print(f'Error exception: {err}')

print(f'Resultado: {resultado}')
