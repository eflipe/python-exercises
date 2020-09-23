'''
In this Kata, you will be given an array of strings and
your task is to remove all consecutive duplicate letters
 from each string in the array.
'''

ejemplo_1 = ["abracadabra","allottee","assessee"]


def dup(arry):
    new_array = []
    for word in arry:
        remove_duplicate = []
        for let in word:
            if remove_duplicate:
                if let == remove_duplicate[-1]:
                    pass
                else:
                    remove_duplicate.append(let)
            else:
                remove_duplicate.append(let)

        new_word = ''.join(remove_duplicate)

        new_array.append(new_word)


dup(ejemplo_1)
# otra
def dup(arry):
    array_new = []
    for string in arry:
        string_new = ""
        prev = None
        for char in string:
            if char != prev:
                string_new += char
            prev = char
        array_new.append(string_new)

    return array_new
