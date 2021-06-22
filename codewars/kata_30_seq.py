'''


73312        => [false, false, true, false, true]
2026         => [false, true, false, true]
635          => [false, false, false]
'''

def divisible_by_last(n):
    # '''
    # Take a number and check each digit if it is divisible by the digit
    # on its left checked and return an array of booleans.
    #
    # The booleans should always start with false becase
    # there is no digit before the first one.
    #
    # :param n: int
    # :return: list
    #
    # >>> divisible_by_last(73312)
    # [false, false, true, false, true]
    #
    # '''
    numbers_str = str(n)
    array_booleans = [False]
    len_numbers_str = len(numbers_str)
    print("PRINT LEN", len_numbers_str)
    for number in range(len_numbers_str):
        if number < len_numbers_str - 1:
            next_num = int(numbers_str[number + 1])
            num = int(numbers_str[number])
            print(next_num)
            print(num)
            if num == 0:
                array_booleans.append(False)
                continue
            if next_num % num == 0:
                array_booleans.append(True)
            else:
                array_booleans.append(False)

    print(array_booleans)
    return array_booleans


def divisible_by_last(n):
    n = str(n)
    res = [False]
    for i in range(1,len(n)):
        if int(n[i-1]) == 0 or int(n[i]) % int(n[i-1]) != 0:
            res.append(False)
        else:
            res.append(True)
    return res

def divisible_by_last(n):
    temp = [False]
    n = str(n)
    for i in range(1, len(n)):
        try:
            if (int(n[i]) / int(n[i-1])).is_integer():
                temp.append(True)
            else:
                temp.append(False)
        except Exception:
            temp.append(False)
    return temp


def divisible_by_last(n):
    res = [False]
    n = str(n)
    for i in range(1, len(n)):
        if n[i-1] == '0':
            res.append(False)
        else:
            res.append(int(n[i]) % int(n[i-1]) == 0)
    return res
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    divisible_by_last(2026)
