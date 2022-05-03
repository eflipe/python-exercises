'''
Link: https://www.codewars.com/kata/54a91a4883a7de5d7800009c
Your job is to write a function which increments a string, to create a new string.

    If the string already ends with a number, the number should be incremented by 1.
    If the string does not end with a number. the number 1 should be appended to the new string.

Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100

Attention: If the number has leading zeros the amount of digits should be considered.

'''

strng_input = "holis"
strng_input_2 = "holis002"
strng_input_3 = '/|52\},SWT1647O(*3{/8508C7(1g~>Xc1"cxI10030305599'
strng_input_4 = "foobar001"
import re

def increment_string_helper(str_input):
    str_split = re.split('(\d+)', str_input)
    print("RES :", str_split)
    str_last_number = str_split[-2]
    print("str_last_number", str_last_number)

    len_number = len(str_last_number)
    number_to_incre = int(str_last_number) + 1
    str_split[-2] = str(number_to_incre).zfill(len_number)
    print("str_split[-2]", str_split[-2])
    join_complete_str = ''.join(str_split)
    print("COMPLETO???", join_complete_str)


    return join_complete_str


def increment_string(strng):
    if strng.isalpha():
        print("Solo letras")
        strng = strng + '1'
        print("WIP: -----", strng_increment)
    else:
        print("Tengo un numerito")
        increment_string_helper(strng)

    return strng


increment_string(strng_input_4)


def increment_string(strng):

    # strip the decimals from the right
    stripped = strng.rstrip('1234567890')

    # get the part of strng that was stripped
    ints = strng[len(stripped):]

    if len(ints) == 0:
        return strng + '1'
    else:
        # find the length of ints
        length = len(ints)

        # add 1 to ints
        new_ints = 1 + int(ints)

        # pad new_ints with zeroes on the left
        new_ints = str(new_ints).zfill(length)

        return stripped + new_ints
