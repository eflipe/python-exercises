print(''.join(reversed(text)))

def reverse_a_string_slowly(a_string):
    new_string = ''
    index = len(a_string)
    while index:
        index -= 1                    # index = index - 1
        new_string += a_string[index] # new_string = new_string + character
    return new_string
    
def reverse_a_string_more_slowly(a_string):
    new_strings = []
    index = len(a_string)
    while index:
        index -= 1
        new_strings.append(a_string[index])
    return ''.join(new_strings)
