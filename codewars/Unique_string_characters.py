"""
solve("xyab","xzca") = "ybzc"
--The first string has 'yb' which is not in the second string.
--The second string has 'zc' which is not in the first string.

"""

str_1 = "xyabb"
str_2 = "xzca"  # output: ybbzc"


def solve(str_1, str_2):
    large_str = str_1 + str_2
    diff_str = ''
    for let in large_str:
        if let in str_1 and let in str_2:
            continue
        diff_str += let
    return diff_str


print(solve(str_1, str_2))


def Diff(li1, li2):
    li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2]
    print(li_dif)
    return li_dif
