people = 'hello'
p_1 = " gap "
p_2 = "two words"


def wave(people):
    wave_list = []
    wave_word = ''
    for char in people:
        if (char.isspace()) == True:
            print('soy un space')
        else:
            print('NO hay space')


wave(p_1)
