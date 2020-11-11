'''
For example the array [2, 3, 9]
equals 239, adding one would return the array [2, 4, 0].
'''


array_1 = [2, 3, 9]
array_2 = [4,3,2,5]
array_3 = [1,-9]
array_4 = [1, 2, 3, 4]


def up_array(arr):

    array_joint = ''

    if not arr:
        return None

    for item in arr:
        if item >= 0 and len(str(item)) == 1:
            array_joint += str(item)
        else:
            return None

    array_joint = int(array_joint) + 1
    array_joint = str(array_joint)

    return [int(item) for item in array_joint]


print(up_array(array_4))
