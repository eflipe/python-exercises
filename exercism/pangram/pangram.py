import string

def is_pangram(sentence):
    sentence = set(sentence.lower())
    if ' ' in sentence:
        sentence.remove(' ')
    elif '_' in sentence:
        sentence.remove('_')
    alphabet = set(string.ascii_lowercase)
    if len(alphabet.intersection(sentence)) == 26:
        return True
    else:
        return False
