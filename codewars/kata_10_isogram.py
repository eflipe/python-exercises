from collections import Counter
string = 'isogram'


def is_isogram(string):

    if string == "":
        return True
    is_iso = Counter(string)
    for val in is_iso.values():
        if val > 1:
            return False
    return True



print(is_isogram(string))