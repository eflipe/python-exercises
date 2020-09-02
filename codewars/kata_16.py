'''
Given a lowercase string that has alphabetic characters only and no spaces,
 return the highest value of consonant substrings. Consonants are any letters
  of the alphabet except "aeiou".

We shall assign the following values: a = 1, b = 2, c = 3, .... z = 26.

For example, for the word "zodiacs", let's cross out the vowels.
We get: "z o d ia cs"
'''
import string

string.ascii_lowercase

s1 = "zodiacs"
s2 = "chruschtschov" # 80
s3 = "twelfthstreet" # 103


def solve(str):
    VOWELS = 'aeiou'
    cnsnnts = []
    vowel_signal = True

    for let in str:
        value = string.ascii_lowercase.index(let) + 1
        if let not in VOWELS and vowel_signal is False:
            cnsnnts[-1] += value

        elif let not in VOWELS:
            cnsnnts.append(value)
            vowel_signal = False

        else:
            vowel_signal = True

    return max(cnsnnts)


print(solve(s2))
