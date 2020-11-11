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
def longest_repetition(chars):

    if len(chars) == 0:
        return '', 0

    the_char = chars[0]
    the_count = 1

    count = 1
    for i in range(1,len(chars)):

        if chars[i-1] == chars[i]:
            count += 1

            if the_count < count:
                the_char = chars[i]
                the_count = count
        else:
            count = 1

    return the_char, the_count


print(longest_repetition(chars))
