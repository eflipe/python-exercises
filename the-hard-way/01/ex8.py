formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format('bla', 'ble', 'bli', 'blu'))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    'pepe',
    'se va',
    'lejos',
    'de aca'
))
