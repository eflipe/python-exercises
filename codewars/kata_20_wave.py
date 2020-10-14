people = 'hello'
p_1 = " gap "
p_2 = "two words"

def wave(people):

    wave_list = []

    for index_people in range(len(people)):
        wave_word = ''
        if wave_list:
            for let in people:
                if index_people == people.index(let) and let.capitalize() not in wave_list[-1]:
                    wave_word += let.capitalize()
                else:
                    wave_word += let

            wave_list.append(wave_word)
        else:
            wave_list.append(people.capitalize())
    print(wave_list)


wave(p_1)
