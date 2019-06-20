"""
Your task is to sort a given string. Each word in the string will contain a
single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string. The words in the input
String will only contain valid consecutive numbers.
"""

sentence = "is2 Thi1s T4est 3a"

sentence2 = "4of Fo1r pe6ople g3ood th5e the2"
sentence3 = ""
# order(sentence)


def order(sentence):
    if sentence == "":
        return sentence
    else:
        sentence_split = sentence.split(' ')
        sentence_list = list(range(len(sentence_split)))

        for word in range(len(sentence_split)):
            for index in sentence_split[word]:
                if index.isdigit():
                    index = int(index) - 1
                    sentence_list[index] = sentence_split[word]

        sentence_list = (' ').join(sentence_list)
    return sentence_list


print(order(sentence2))
"""
Otras soluciones:

def order(s):
    z = []
    for i in range(1,10):
        for j in list(s.split()):
            if str(i) in j:
               z.append(j)
    return " ".join(z)


"""
