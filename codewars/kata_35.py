'''
In this kata you are required to, given a string, replace every letter
with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

'''
import string


def alphabet_position(text):
    alphabet_string = string.ascii_lowercase
    alphabet_list = list(alphabet_string)  # no es necesario hacerlo una lista
    string_with_positions = ''

    for letter_text in text.lower():
        if letter_text in alphabet_string:
            string_with_positions += f'{alphabet_list.index(letter_text) + 1} '

    return string_with_positions


# otras
def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())



if __name__ == '__main__':
    text = "The sunset sets at twelve o' clock."
    text_2 = "The narwhal bacons at midnight."
    output = alphabet_position(text_2)
    print(output)
