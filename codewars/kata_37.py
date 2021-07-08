"""
You will be given a vector of strings.
You must sort it alphabetically
(case-sensitive, and based on the ASCII values of the chars)
and then return the first value.

The returned value must be a string, and have "***" between
each of its letters.

You should not remove or add elements from/to the array.

"""


def two_sort(array):
    array_sorted = sorted(array)
    first_value = array_sorted[0]
    first_value_to_list = list(first_value)
    join_first_value = "***".join(first_value_to_list)

    return join_first_value


# otras soluciones
def two_sort(arr):
    return '***'.join(sorted(arr)[0])

def two_sort(a):
    a.sort()
    b=a[0]
    b='***'.join(b)
    return b

if __name__ == "__main__":
    text = ["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"]  # 'b***i***t***c***o***i***n'
    text_2 = ["turns", "out", "random", "test", "cases", "are", "easier", "than", "writing", "out", "basic", "ones"]  # 'a***r***e'
    text_3 = ["Lets", "all", "go", "on", "holiday", "somewhere", "very", "cold"]  # 'L***e***t***s'
    text_4 = ["i", "want", "to", "travel", "the", "world", "writing", "code", "one", "day"]  # 'c***o***d***e'
    text_5 = "java script"
    output = two_sort(text_4)
    print(output)
