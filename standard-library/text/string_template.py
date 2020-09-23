import string

values = {'var': 'foo'}
t = string.Template("""
    Variable : $var
    Escape : $$
    Variable in text: ${var}iable
""")
print('TEMPLATE:', t.substitute(values))

s = """
Variable : %(var)s
Escape : %%
Variable in text: %(var)siable
"""
print('INTERPOLATION:', s % values)

s = """
Variable : {var}
Escape : {{}}
Variable in text: {var}iable
"""
print('FORMAT:', s.format(**values))

values = {'var': 'foo'}
t = string.Template("$var is here but $missing is not provided")
try:
    print('substitute() :', t.substitute(values))
except KeyError as err:
    print('ERROR:', str(err))
    print('safe_substitute():', t.safe_substitute(values))
