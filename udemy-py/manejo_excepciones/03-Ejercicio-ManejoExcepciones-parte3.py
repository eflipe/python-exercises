resultado = None
try:
    a = int(input("Primer número: "))
    b = int(input("Segundo número: "))
    resultado = a / b
except ZeroDivisionError as e:
    print("Ocurrió un error con ZeroDivisionError", e)
    print(type(e))
except TypeError as e:
    print("Ocurrió un error con TypeError", e)
    print(type(e))
#except ValueError as e:
#    print("Ocurrió un error con ValueError", e)
#    print(type(e))
except Exception as e:  # clase de maypr jerarquia
    print("Ocurrió un error con exception", e)
    print(type(e))

print("resultado: ", resultado)
print("continuamos...")
