# Remove the parentheses
s = "example(unwanted thing)example" # "exampleexample"
s_2 = "example (unwanted thing) example" # "example  example"
s_3 = "a (bc d)e"
s_4 = "a(b(c))" # a
s_5 = "(first group) (second group) (third group)" # "  "


def remove_parentheses(s):
    c = 0
    res = ''
    for e in s:
        if e == '(': c += 1
        if e == ')': c -= 1
        if c == 0: res += e
    return res.replace(')', '')


def remove_parentheses(s):
    nested = 0
    result = []
    for c in s:
        if c == "(":
            nested += 1
        elif c == ")":
            nested -= 1
        elif nested == 0:
            result.append(c)
    return "".join(result)
