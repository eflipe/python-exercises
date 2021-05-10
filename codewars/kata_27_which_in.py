# https://www.codewars.com/kata/550554fd08b86f84fe000a58
a1 = ["live", "arp", "strong"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]


def in_array(array1, array2):
    new_array = []
    for word_a1 in array1:
        for word_a2 in array2:
            if word_a1 in word_a2 and word_a1 not in new_array:
                new_array.append(word_a1)

    print(new_array)
    new_array.sort()

    return print(new_array)


in_array(a1, a2)

# otra
# def in_array(array1, array2):
#     array2 = ' '.join(array2)
#     return sorted(set(a for a in array1 if a in array2))


def in_array(array1, array2):
    result = set()
    for a in array1:
        for b in array2:
            if a in b:
                result.add(a)
                break
    return sorted(result)
