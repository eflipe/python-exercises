def disemvowel(string):
    vowels = 'aeiouAEIOU'


    for vowel in vowels:
        string = string.replace(vowel, '')



    return string

def disemvowel(s):
    return s.translate(None, "aeiouAEIOU")
