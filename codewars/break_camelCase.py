
str_camelcase = "breakCamelCase" # "break Camel Case"


def break_camelCase(s):
    break_string = []
    index_start = 0

    for index, let in enumerate(s):
        if let.isupper():
            break_string.append(s[index_start:index])
            index_start = index
        if index == len(s) - 1:
            break_string.append(s[index_start:])

    return (' ').join(break_string)


print(break_camelCase(str_camelcase))
def solution(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)

def solution(s):
    newStr = ""
    for letter in s:
        if letter.isupper():
            newStr += " "
        newStr += letter
    return newStr

def solution(s):
    st = ""

    for c in s:
        if c.upper() == c:
            st += " " + c
        else:
            st += c

    return st
