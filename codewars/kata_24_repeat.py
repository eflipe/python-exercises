chars = "aaaabb"
# ('a', 4)
chars_2 = "cbdeuuu900"
# ('u', 3)
'''
For a given string s find the character c (or C) with longest consecutive repetition and return:

(c, l)

// proceso:
contar cada char

//output
chat que más se repite
'''


def longest_repetition(chars):
    char_dict = {}
    for char in chars:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1

    max_value = max(char_dict.values())

    for key, value in char_dict.items():
        if value == max_value:
            return (key, value)



print(longest_repetition(chars_2))
