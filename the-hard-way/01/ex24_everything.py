print('Escapar apostrofes \' otro mas \' y esto tambien \\ tambien saber sobre: ')
print('\n nuevas líneas y tabs: \t tabs')

text = """
\t tab de ejemplo
texto largo que dice algo profundo
una nueva linea \n y luego seguimos
escribiedo este hermoso idioma
algunas letras más
\n\t\tnueva lìnea y dos tabs 

"""
print("-------------")
print(text)
print("-------------")


def formula_secreta(inicio):
    jelly_beans = inicio * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

inicio_inicial = 10000
beans, jars, crates = formula_secreta(inicio_inicial)

print("Cifra de inicio: {}".format(inicio_inicial))
print(f'num 1: {beans}, num 2: {jars}, num 3: {crates}. ')
# con *
formula = formula_secreta(inicio_inicial)
print('Formula (devulve una lista): ', formula)
print('Otra forma usando la *: num 1: {}, num 2: {}, num 3: {}. \n'
      'aplicas una list a un format string'.format(*formula))