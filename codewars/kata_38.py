# https://www.codewars.com/kata/57f6051c3ff02f3b7300008b/train/python


def meeting(rooms, number):
    chairs_array = []
    sum_chairs_array = 0

    if number == 0:
        return "Game On"

    for room in rooms:
        room_occupants = len(room[0])
        rooms_chairs = room[1]
        chairs_diff = rooms_chairs - room_occupants

        if sum_chairs_array >= number:
            number_diff = sum_chairs_array - number
            chairs_array[-1] = chairs_array[-1] - number_diff
            break
        if chairs_diff <= 0:
            chairs_array.append(0)
        else:
            chairs_array.append(chairs_diff)

        sum_chairs_array = sum(chairs_array)

    if sum(chairs_array) < number:
        return "Not enough!"

    return chairs_array


# otra
def meeting(rooms, number):
    #     print(f'number is {number}, room is {rooms}')
    if number == 0:
        return "Game On"
    ans = []
    index = 0
    while number > 0:
        #         print('len rooms is', len(rooms))
        if index == len(rooms):
            return "Not enough!"
        remain = rooms[index][1] - len(rooms[index][0])
        if remain < 0:
            ans.append(0)
            index = index + 1
            continue
        if number - remain >= 0:
            ans.append(remain)
            number = number - remain
            index = index + 1
        else:
            ans.append(number)
            number = 0
    return ans
    # your code here


if __name__ == "__main__":
    rooms = [["XXX", 3], ["XXXXX", 6], ["XXXXXX", 9]]
    number = 4  # [0, 1, 3]
    rooms_2 = [["XXX", 1], ["XXXXXX", 6], ["X", 2], ["XXXXXX", 8], ["X", 3], ["XXX", 1]]
    number_2 = 5  #  [0, 0, 1, 2, 2]
    rooms_3 = [["XX", 2], ["XXXX", 6], ["XXXXX", 4]]
    number_3 = 0
    rooms_4 = [["XX", 2], ["XXXX", 6], ["XXXXX", 4]]
    number_4 = 8
    rooms_5 = (
        ["XXX", 3],
        ["XXX", 9],
        ["XXXXXXXX", 7],
        ["X", 10],
        ["XX", 0],
        ["XXXXXXXXXX", 1],
    )
    number_5 = 5  # [0, 5]
    rooms_6 = [
        ["XXXXXXX", 2],
        ["XXXXXXXXXX", 2],
        ["XXXXX", 9],
        ["XXXXXXX", 8],
        ["XXXX", 10],
        ["X", 6],
    ]
    number_6 = 7
    rooms_7 = [["XXXXXXXXX", 8], ["XXX", 10], ["XXXXXXXXXX", 4], ["XXXXXXX", 10]]
    number_7 = 8
    output = meeting(rooms_7, number_7)
    print(output)
