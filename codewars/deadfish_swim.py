# https://www.codewars.com/kata/51e0007c1f9378fa810002a9/train/python

"""
Deadfish has 4 commands, each 1 character long:

i increments the value (initially 0)
d decrements the value
s squares the value
o outputs the value into the return array

"""

input = "isoisoiso" # [1,4,25]
input_2 = "idoiido" # [0,1]
input_3 = "codewars"

def parse(data):
    output_array = []
    count = 0
    for cmd in data:
        if cmd == 'i':
            count += 1
        elif cmd == 's':
            count = count ** 2
        elif cmd == 'd':
            count -= 1
        elif cmd == 'o':
            output_array.append(count)

    return output_array

print(parse(input_3))
