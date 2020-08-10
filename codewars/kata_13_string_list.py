names = ['Alex', 'Jacob', 'Mark', 'Max']  # 'Alex, Jacob and 2 others like this'
names_1 = ['Max', 'John', 'Mark'] # 'Max, John and Mark like this'
names_2 = ['Jacob', 'Alex']  # 'Jacob and Alex like this'
names_5 = ['Peter'] # 'Peter likes this'
names_4 = []  # 'no one likes this'


def likes(names):

    if not names:
        return print('no one likes this')

    elif len(names) == 1:
        return print(f'{names[0]} likes this')

    elif len(names) == 2:
        return print(f'{names[0]} and {names[1]} like this')

    elif len(names) == 3:
        return print(f'{names[0]}, {names[1]} and {names[2]} like this')

    else:
        return print(f'{names[0]}, {names[1]} and {len(names[2:])} others like this')

# otra
def likes(names):
    count = len(names)

    if count == 0:
        return "no one likes this"
    elif count == 1:
        return names[0] + " likes this"
    elif count == 2:
        return ' and '.join(names) + " like this"
    elif count == 3:
        return names[0] + ", " + ' and '.join(names[1:]) + " like this"
    else:
        return ', '.join(names[:2]) + " and " + str(count - 2) + " others like this"



likes(names_4)