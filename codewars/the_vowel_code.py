# https://www.codewars.com/kata/53697be005f803751e0015aa/train/python

text = 'How are you today?' # 'H4w 1r2 y45 t4d1y?'
text_2 = 'This is an encoding test.'

vowels_dict = {
        'a': '1',
        'e': '2',
        'i': '3',
        'o': '4',
        'u': '5'
}


def encode(st):
    for vowel in vowels_dict.keys():
        st = st.replace(vowel, vowels_dict[vowel])
    return st

def decode(st):
    for vowel, number in vowels_dict.items():
        st = st.replace(number, vowel)
    return st

print(encode(text_2))
print(decode(text_2))
def encode(s, t=str.maketrans("aeiou", "12345")):
    return s.translate(t)

def decode(s, t=str.maketrans("12345", "aeiou")):
    return s.translate(t)

def encode(st):
    for i, v in enumerate("aeiou", start=1):
        st = st.replace(v,str(i))
    return st

def decode(st):
    for i, v in enumerate("aeiou", start=1):
        st = st.replace(str(i),v)
    return st
