string_1 = "bmwvolvoBMW" # volvo
string_2 = "blablahblah" # lalahlah
string_3 = 2525637
string_4 = "bmwVolVoBMW"


def remove_bmw(string):
    if type(string).__name__ == 'str':
        string_list = list(string)
        for char in string:
            if char.lower() == 'b' or char.lower() == 'm' or char.lower() == 'w':
                string_list.remove(char)
        return ''.join(string_list)
    else:
        raise TypeError("This program only works for text.")


print(remove_bmw(string_4))

# otra
def remove_bmw(string):
    for x in list('BbMmWw'):
        try:
            string = string.replace(x, '')
        except AttributeError:
            return "This program only works for text."
    return string

# otra
