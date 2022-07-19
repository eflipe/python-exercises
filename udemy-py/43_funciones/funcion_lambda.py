# son funciones pequeñas y anonimas (sin nombre)

mi_funcion_lambda = lambda a, b: a + b

print(mi_funcion_lambda(4, 6))

# funcion lamda que no recibe argumnetos
mi_funcion_lambda = lambda: 'funcion sin argumentos'

# parametros por default
mi_funcion_lambda = lambda a=5, b=6: a + b
print(mi_funcion_lambda())

# funcion lambda con argumentos variables *args y **kwargs
mi_funcion_lambda = lambda *args, **kwargs: f'Len args: {len(args)}, len kwargs: {len(kwargs)}'
# args = tupla, kwargs = dict
print(mi_funcion_lambda(1, 2, 2, a=1, b=2))  # se pasa un dict de dos elemntos

# Funciones lambda con argumentos, argumentos variables y valores por default
mi_funcion_lambda = lambda a, b, c=3, *args, **kwargs: a+b+c+len(args)+len(kwargs)
print(f'Resultado función lambda: {mi_funcion_lambda(1,2,4,5,6,7,e=5,f=7)}')
