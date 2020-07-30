'''
counts the number of occurrences of each letter in a string.

'''
import pprint


message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for char in message:  # char: letra por letra
    count.setdefault(char, 0)  # si ya existe te tira el valor guardado
    count[char] += 1

pprint.pprint(count)
print(pprint.pformat(count))
