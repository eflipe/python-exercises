string = 'CodeWars is nice' # ##CodewarsIsNice
string_1 = 'c i n'


def generate_hashtag(string):

    if not string:
        return False

    word_split = string.lower().title().split(' ')
    word_hashtag = ('').join(word_split)

    if len(word_hashtag) > 140:
        return False

    return f'#{word_hashtag}'

# otra
def generate_hashtag(s):
    output = "#"

    for word in s.split():
        output += word.capitalize()

    return False if (len(s) == 0 or len(output) > 140) else output

# otra
def generate_hashtag(s):
    if len(s) == 0 or len(s) > 140:
        return False
    return f"#{''.join([w.capitalize() for w in s.split()])}"

print(generate_hashtag(string_1))
