'''
Link: https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d/train/python
Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

Examples:

solution('abc', 'bc') # returns true
solution('abc', 'd') # returns false

'''


def solution(string, ending):
    end_value = len(string)
    print('end', end_value)
    ends_with = string.endswith(ending, 0, end_value)
    return ends_with


if __name__ == '__main__':
    string_test_1 = 'abc'
    end_test_1 = 'bc'
    string_test_2 = 'abc'
    end_test_2 = 'd'
    string_test_3 = 'abc'
    end_test_3 = 'abc'
    print(solution(string_test_3, end_test_3))
