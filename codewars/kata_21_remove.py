# Remove the parentheses
s = "example(unwanted thing)example" # "exampleexample"
s_2 = "example (unwanted thing) example" # "example  example"
s_3 = "a (bc d)e"
s_4 = "a(b(c))" # a
s_5 = "(first group) (second group) (third group)" # "  "

def remove_parentheses(s):
    remove_prnthss = ''
    index_1 = 0
    index_2 = 0
    count_1 = 0
    count_2 = 0

    for index, let in enumerate(s):
        
        if let.startswith('(') and index_1 == 0:
            index_1 = index
            count_1 += 1
        if let.endswith(')') and (count_2 + 1) == count_1:
            index_2 = index
            count_2 += 1
            remove_prnthss += s[0:index_1] + s[index_2+1:]


    remove_parentheses = s[0:index_1] + s[index_2+1:]


    return remove_parentheses


print(remove_parentheses(s_5))
