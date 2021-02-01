"""
high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"

"""

numbers = "4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"
numbers_1 = "1 -1"


def high_and_low(numbers):
    numbers += ' '
    numbers_list = []
    number = ''
    for num in numbers:
        number += num
        if num == ' ':
            print('NUM', num)
            print('NUMBER', number)
            numbers_list.append(int(number))
            number = ''
    print(numbers_list)
    max_number = max(numbers_list)
    min_number = min(numbers_list)
    print(min_number)
    number_str = f'{max_number} {min_number}'
    return number_str


print(high_and_low(numbers_1))

def high_and_low(numbers): #z.
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn),min(nn))

def high_and_low(numbers):
    n = map(int, numbers.split(' '))
    return "{} {}".format(max(n), min(n))

def high_and_low(numbers):
    # ...
    numbers = [int(x) for x in numbers.split()]
    ma, mi = str(max(numbers)), str(min(numbers))

    return ma +" " + mi

def high_and_low(numbers):
    #split the string of numbers on spaces
    new_num = numbers.split(" ")
    num_list = []

    #turn string of numbers into a list of integers
    for num in new_num:
        num_list.append(int(num))

    #grab minimum and maximums
    min_num = str(min(num_list))
    max_num = str(max(num_list))

    return max_num + " " + min_num
