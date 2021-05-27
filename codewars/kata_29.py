# https://www.codewars.com/kata/5f6d120d40b1c900327b7e22/train/python
leaderboard = ['John', 'Brian', 'Jim', 'Dave', 'Fred']
changes = ['Dave +1', 'Fred +4', 'Brian -1']


def leaderboard_sort(leaderboard, changes):
    print("Board inicial: ", leaderboard)
    split_changes = []
    new_leaderboard = []
    for name in changes:
        split_name = name.split(' ')
        split_changes.append(split_name)

    for x, y in split_changes:
        print(y)

    leaderboard_copy = leaderboard.copy()
    for name_split in split_changes:
        #print(f'INDEX: {index} NAME: {name}')
        for index, name in enumerate(leaderboard):

            if name == name_split[0]:
                print("Name: ", name_split[0])
                print('Current index: ', index)
                print('Change: ', name_split[1])
                new_index = index + -(int(name_split[1]))
                print('new index: ', new_index)
                leaderboard.remove(name)
                leaderboard.insert(new_index, name)
                print("Board parcial: ", leaderboard)
                break


    print("Board final: ", leaderboard)




leaderboard_sort(leaderboard, changes)

def leaderboard_sort(leaderboard, changes):
    for change in changes:
        name, move = change.split()
        value_index = leaderboard.index(name)

        leaderboard.remove(name)
        leaderboard.insert(value_index - int(move), name)

    return leaderboard

def leaderboard_sort(leaderboard, changes):
    change, arr = [x.split() for x in changes], leaderboard
    for name, i in change:
        idx = arr.index(name) - int(i)
        arr.remove(name)
        arr.insert(idx, name)
    return arr
