from typing import KeysView

pepe = [12, 45, 'pepe', 'miguel', 6]
print(pepe)
print(len(pepe))

paar = "Hola pepe"

pepe.append(paar)

print(pepe)

my_dict = {
    "ejemplo": "valor",
    "otro": 22,
}

print(my_dict['ejemplo'])
print(my_dict.keys())
to_list = list(my_dict.keys())
print(to_list)
print(to_list[1])
my_dict['otro_mas'] = 222
print(my_dict)
