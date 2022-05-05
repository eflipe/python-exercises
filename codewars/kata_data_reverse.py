'''
Link: https://www.codewars.com/kata/569d488d61b812a0f7000015
'''
data_array = [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]
data_array_2 = [0,0,1,1,0,1,1,0,0,0,1,0,1,0,0,1]
reversed_list = data_array[::-1]


def data_reverse(data):
    data_list = []
    BITS_LONG = 8

    for index, number in enumerate(data):
        if index % BITS_LONG == 0:
            print("HOLISSSSS, 4 veces?", index)
            print("slicing", data[index:index + BITS_LONG])
            data_list = data[index:index + BITS_LONG] + data_list


data_reverse(data_array_2)
