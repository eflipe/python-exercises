import string

st = "I, habitan of the Alleghanies, treating of him as he is in himself in his own rights"
st_2 = ", , !! . ."

def pseudo_sort(st):

    let_upper = []
    let_lower = []

    # for ch in string.punctuation:
    #     st = st.replace(ch, '')

    word_list = sorted(st.split(' '))
    for let in word_list:
        if let[0].isupper():
            let_upper.insert(0, let)
        else:
            let_lower.append(let)

    word_sort = let_lower + let_upper
    word = " ".join(word_sort)

    for ch in string.punctuation:
         word = word.replace(ch, '')
    print(word)


pseudo_sort(st_2)

#otra

# def pseudo_sort(st):
#     words = st.translate(str.maketrans("", "", ".,:;!?")).split()
#     lower, upper = [], []
#
#     for word in words:
#         if word[0].isupper():
#             upper.append(word)
#         else:
#             lower.append(word)
#
#     return " ".join(sorted(lower) + sorted(upper, reverse=True))

# from re import findall
#
# def pseudo_sort(st):
#     lows = sorted(findall(r'\b[a-z]+\b', st))
#     ups  = sorted(findall(r'[A-Z][A-Za-z]*', st), reverse=True)
#     return ' '.join(lows + ups)