import load_dict
import time

word_list = load_dict.load('palabras_todas.txt')

start_time = time.time()


def find_palingrams():
    pali_list = []
    for word in word_list:
        end = len(word)
        rev_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end-i] and rev_word[end-i:] in word_list:
                    pali_list.append((word, rev_word[end-i:]))
                    # print(f'word[i:]: {word[i:]}')
                    # print(f'rev_word[:end-i]: {rev_word[:end-i]}')
                    # print(f'rev_word[end-i:]: {rev_word[end-i:]}')
                    # print(f'Palabra guardada: {word}, {rev_word[end-i:]}')

                if word[:i] == rev_word[end-i:]and rev_word[:end-i]in word_list:
                    pali_list.append((rev_word[:end-i], word))

    return pali_list


end_time = time.time()

palingrams = find_palingrams()

palingrams_sorted = sorted(palingrams)

print("\nNumber of palingrams = {}\n".format(len(palingrams_sorted)))
for first, second in palingrams_sorted:
    print("{} {}".format(first, second))

dif = end_time - start_time
print("Runtime for this program was {} seconds.".format(dif))
