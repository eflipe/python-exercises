# boolean

ex_16 = not (1 != 10 or 3 == 4)
print(ex_16)

ex_17 = not ("testing" == "testing" and "pepe" == "fulano")
print(ex_17)

ex_18 =  1 == 1 and (not ("testing" == 1 or 1 == 0))
print(f'18: {ex_18}')

ex_19 = "pepe" == "fulano" and (not (3 == 4 or 3 == 3))
print(f'19: {ex_19}')

ex_20 = 3 == 3 and (not ("pepe" == "pepe" or "pepe" == "miguel"))
print(f'20: {ex_20}')