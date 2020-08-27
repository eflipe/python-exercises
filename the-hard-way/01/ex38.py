diez_cosas = "Uno Dos Tres Cuatro Cinco Seis"
cosas = diez_cosas.split(' ')

mas_cosas = ["Siete", "Ocho", "Nueve", "Diez", "Once"]

while len(cosas) != 10:
    next_one = mas_cosas.pop()
    print("Agregando: ", next_one)
    cosas.append(next_one)
    print(f"Ahora hay {len(cosas)} cosas. El ùtlimo item agreagdo fue {next_one}")

print("Todo: ", cosas)

print(cosas[1])
print(cosas[-1])
print(cosas.pop())
print(' '.join(cosas))
print('#'.join(cosas[3:5]))

