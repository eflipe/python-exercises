'''
The vowel substrings in the word codewarriors are o,e,a,io. The longest of these has a length of 2. Given a lowercase string that has alphabetic characters only (both vowels and consonants) and no spaces, return the length of the longest vowel substring. Vowels are any of aeiou

- junto las las letras (v_seq)
    - si es vocal y esta en v_seq + 1


'''

s = "suoidea" # 3


def solve(s):
    vowels = 'aeiou'
    v_count = 0
    result = []

    for v in s:
        if v in vowels:
            v_count += 1
        else:
            result.append(v_count)
            v_count = 0

    result.append(v_count)

    print(max(result))


solve(s)
