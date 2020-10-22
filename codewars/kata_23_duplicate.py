s = 'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'
# 'alpha beta gamma delta alpha beta gamma delta'


def remove_consecutive_duplicates(s):
    string_words = s.split()
    no_duplicates_list = []

    for word in string_words:
        if no_duplicates_list:
            if word == no_duplicates_list[-1]:
                continue

        no_duplicates_list.append(word)

    return ' '.join(no_duplicates_list)

print(remove_consecutive_duplicates(s))


def remove_consecutive_duplicates(s):
    results =[]
    for word in s.split():
        if word not in results:
            results.append(word)
        elif results[-1] != word:
            results.append(word)
    return ' '.join(results)
