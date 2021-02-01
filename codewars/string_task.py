string_1 = 'aBAcAba'


def string_task(s):
    s_lower = s.lower()
    new_s = ''
    vowels = "aeiouy"
    for let in s_lower:
        if let not in vowels:
            new_s += '.' + let

    return new_s


print(string_task(string_1))

def string_task(s):
    return ''.join(f'.{a}' for a in s.lower() if a not in 'aoyeui')
