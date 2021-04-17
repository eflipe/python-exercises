resultado = None
a = "10"
b = 1

try:
    resultado = a / b
except Exception as e:
    print("Tenemos un error.", e)
    print(type(e))

print("Resultado: ", resultado)
print("Seguimos....")
