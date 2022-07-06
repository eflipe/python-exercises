from clases_excepciones_personalizadas import NumerosIdenticosException


resultado = None
try:
    a = int(input("Primer numero: "))
    b = int(input("Segundo numero: "))
    if a == b:
        # raise tira cualquier tipo de excepcion
        raise NumerosIdenticosException("Los números son iguales.")

    resultado = a / b

except ZeroDivisionError as err:
    print(f'Error division por zero: {err}, {type(err)}')

except TypeError as err:
    print(f'Error type error: {err}')

except Exception as err:
    print(f'Error exception: {err}')
else:
    # se ejecuta si no ocurrio ninguna excepcion
    print("No hubo errores")
finally:
    # este bloque siempre se ejecuta
    print("Ejecucion bloque finally")

print(f'Resultado: {resultado}')
