"""
There are 32 letters in the Polish alphabet: 9 vowels and 23 consonants.

Your task is to change the letters with diacritics:

ą -> a,
ć -> c,
ę -> e,
ł -> l,
ń -> n,
ó -> o,
ś -> s,
ź -> z,
ż -> z
and print out the string without the use of the Polish letters.

For example:

"Jędrzej Błądziński"  -->  "Jedrzej Bladzinski"
"""

polish_dict = {
            'ą': 'a',
            'ć': 'c',
            'ę': 'e',
            'ł': 'l',
            'ń': 'n',
            'ó': 'o',
            'ś': 's',
            'ź': 'z',
            'ż': 'z',
}

name = "Jędrzej Błądziński"


def correct_polish_letters(name):

    name = list(name)
    for l in range(len(name)):
        for polish_keys, polish_values in polish_dict.items():
            if name[l] == polish_keys:
                name[l] = polish_values

    new_name = ('').join(name)

    return new_name

correct_polish_letters(name)

# Otras soluciones
def correct_polish_letters(s):
    return s.translate(str.maketrans("ąćęłńóśźż", "acelnoszz"))

# Otras
def correct_polish_letters(st):
    l = "ąćęłńóśźż"
    lt = "acelnoszz"
    for i in range(len(l)):
        st = st.replace(l[i], lt[i])
    return st

name = "Jędrzej Błądziński"
def correct_polish_letters(st):
    alphabet = {'ą':'a', 'ć':'c', 'ę':'e', 'ł':'l', 'ń':'n',
                'ó':'o', 'ś':'s', 'ź':'z', 'ż':'z'}

    result = ''
    for i in st:
        print('i =', i)
        if i in alphabet:
            print('i alpha', i)
            result += alphabet[i]
        else:
            result += i

    return print(result)

correct_polish_letters(name)

# otra
def correct_polish_letters(zdanie):

    for k, v in letters.items():
        zdanie = zdanie.replace(k, v)

    return zdanie
