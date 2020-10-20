string_1 = "bmwvolvoBMW" # volvo
string_2 = "blablahblah" # lalahlah
string_3 = 2525637


def remove_bmw(string):

    print(type(string))

    #if (isinstance(string, str)):
    if type(string).__name__ == 'str':
        string_lower = string.lower()
        string_list = list(string_lower)
        for char in string_lower:
            print(char, end=',')
            if char == 'b' or char == 'm' or char == 'w':
                string_list.remove(char)
        return string_list
    else:
        raise ValueError("This program only works for text.")


print(remove_bmw(string_3))
