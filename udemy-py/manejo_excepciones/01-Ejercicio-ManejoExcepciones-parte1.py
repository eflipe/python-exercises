# Try - exception: para evitar que el programa termine de forma abrupta

try:
    10/0
except Exception as e:
    print("Ocurrió un error", e)

print("continuamos")
