
text_1 = 'dont you talk tome' # 'D*NT!!!! Y**!!!! T@LK!!!! T*M*!!!!'


def gordon(word):
    vowels = 'aeiou'
    final_word = ''
    split_word = list(word.lower())
    for let in split_word:
        if let == 'a':
            let = '@'
        elif let in vowels:
            let = '*'
        elif let.isspace():
            let = '!!!! '

        final_word += let.upper()


    return final_word + '!!!!'

def gordon(a):
    return '!!!! '.join(a.upper().split()).translate(str.maketrans('AEIOU', '@****'))+'!!!!'

def gordon(a):
    a=a.upper()
    a=a.replace(' ', '!!!! ')
    a=a.replace('A', '@')
    vowels = ['E', 'I', 'O', 'U']
    for each in vowels:
        a=a.replace(each, '*')
    return a + '!!!!'

def gordon(s):
    out = ''
    for c in s.upper():
        if c == 'A':
            out += '@'
        elif c in 'EIOU':
            out += '*'
        elif c == ' ':
            out += '!!!! '
        else:
            out += c
    return out + '!!!!'

print(gordon(text_1))
