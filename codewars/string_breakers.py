# https://www.codewars.com/kata/59d398bb86a6fdf100000031
'''
n = 5;

st = "This is an example string";

Return value:
Thisi
sanex
ample
strin
g

Return value as a string: 'Thisi'+'\n'+'sanex'+'\n'+'ample'+'\n'+'strin'+'\n'+'g'
'''

n = 5
# n = 8

st = 'This is an example string'
st_2 = 'lyzlhhvtl9bz6xfu'


def string_breakers(n, st):
    st_split = st.split()
    st_join = ('').join(st_split)
    st_new = ''
    index_start = 0
    index_end = n
    len_st = (len(st_join) - 1)

    for index, let in enumerate(st_join):
        if index == index_end:
            st_new += st_join[index_start:index_end] + '\n'
            index_end += n
            index_start += n
        if index == len_st:
            print("SI")
            st_new += st_join[index_start:]

    return st_new


print(string_breakers(n, st))

# otros
def string_breakers(n, st):
    s = st.replace(' ', '')
    return '\n'.join(s[i:i+n] for i in range(0, len(s), n))

def string_breakers(n, st):
    pos = 0
    result = ''
    st = st.replace(' ', '')
    while pos <= len(st):
        result += st[pos:pos + n] + "\n"
        pos += n
    result = result.rstrip()

    return result
