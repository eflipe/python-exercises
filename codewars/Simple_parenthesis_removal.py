math_string = 'u-(v-w-(x+y))-z'
str_2 = "x-(-y-z)"


def solve(s):

    w_p = s.split('(')
    w_p_2 = ''.join(w_p)

    w_p_final = w_p_2.split(')')
    w_p_final_join = ''.join(w_p_final)


    return w_p_final_join


print(solve(str_2))
