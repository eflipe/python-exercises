"""Find palindromes (letter palingrams) in a dictionary file."""
import load_dict
word_list = load_dict.load('dictionary.txt')
pali_list = []

for word in word_list:
    if len(word) > 1 and word == word[::-1]:
        pali_list.append(word)

print("\nTotal de palíndromos encontrados = {}\n".format(len(pali_list)))
print(*pali_list, sep='\n')
# *:  splat operator, which takes a list as input
# and expands it into positional arguments in the function call.
