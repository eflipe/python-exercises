text = """In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income."""
text_2 = "a a a  b  c c  d d d d  e e e e e"
text_3 = "e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"
text_4 = "  //wont won't won't "
text_5 = "  , e   .. "
text_6 = "  ...  "
text_7 = "  '''  "
from collections import Counter


def top_3_words(text):

    for index, let in enumerate(text):
        if not let.isalpha() and let != "'":
            text = text.replace(let, ' ')

    text = text.lower().split()
    list_top_3 = []

    text_counter = Counter(text)
    top_3 = text_counter.most_common()
    if len(top_3) >= 3:
        for item in range(3):
            list_top_3.append(top_3[item][0])
    else:
        for item in range(len(top_3)):
            if top_3[item][0].count("'") >= 2:
                continue
            list_top_3.append(top_3[item][0])

    return list_top_3


print(top_3_words(text_7))
