from sys import argv

script, user_name = argv

prompt = '> '

print(f'Var 1: {script}. Var 2: {user_name}')
print(f'Pregunta para {user_name}: ')
var_input_1 = input(prompt)
print(f'Otra pregunta para {user_name}: ')
var_input_2 = input(prompt)

print(f"""
Los valores ingresados fueron: 
{var_input_1},
{var_input_2},
Adiòs!
""")