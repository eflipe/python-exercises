#a = int(input("Proporciona un valor:"))
a = 3
valorMinimo = 0
valorMaximo = 5
dentroRango = (a >= valorMinimo and a <= valorMaximo)
# and: TODOS los valares tiene que ser verdaderos
#print(dentroRango)
if(dentroRango):
    print("dentro de rango")
else:
    print("fuera de rango")


vacaciones = True
diaDescanso = False
if(vacaciones or diaDescanso):
    print("Puedes ir al parque")
else:
    print("Tienes deberes que hacer")

# OR: es False si todos los valores son false

#if(not(vacaciones or diaDescanso)):
#     print("Tienes deberes que hacer")
#else:
#    print("Puedes ir al parque")

#print(not(vacaciones))
