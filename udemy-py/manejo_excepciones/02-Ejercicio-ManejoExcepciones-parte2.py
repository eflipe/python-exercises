from error_personalizado import ErrorNumerosIdenticosException

resultado = None
a = 1
b = 1
try:
    resultado = a / b

    if a == b:
        # raise ErrorNumerosIdenticosException('Números iguales no permitidos')
        raise ValueError("Error de valor")
# Primero se pone la excepcion de menos jerarquia
except ZeroDivisionError as e:
    print("Ocurrió un error con ZeroDivisionError: ", e)
    print(type(e))
except TypeError as e:
    print("Ocurrió un error con TypeError: ", e)
    print(type(e))
except Exception as e:
    print("Ocurrió un error con exception: ", e)
    print(type(e))

print("resultado: ", resultado)
print("continuamos...")
