people = 'hello'
p_1 = " gap "
p_2 = "two words"


def wave(people):

    wave_list = []
    people_strip = people.strip()

    for let_strip in range(len(people)):
        wave_word = ''
        if people[let_strip] == ' ':
            wave_word += people[let_strip]
            continue
        for let in range(len(people)):
            if let_strip == let:
                wave_word += people[let].capitalize()
            else:
                wave_word += people[let]
        wave_list.append(wave_word)
    print(wave_list)
    return wave_list


wave(p_1)

# otra
def wave(words):
    result = []
    chars = list(words)
    for index, char in enumerate(chars):
        if char.isalpha():
            copy = chars[:]
            copy[index] = copy[index].upper()
            result.append(''.join(copy))
    return result
