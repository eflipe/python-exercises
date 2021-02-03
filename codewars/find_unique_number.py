arr = [ 3, 10, 3, 3, 3 ] # 10

from collections import deque
from collections import Counter

def find_uniq(arr):
    arr_counter = Counter(arr)
    print(arr_counter)
    for number in arr_counter:
        if arr_counter[number] == 1:
            break

    return number


# print(find_uniq(arr))

def find_uniq(arr):
    s = set(arr)
    print("SET", s)
    for e in s:
        if arr.count(e) == 1:
            return e

print(find_uniq(arr))
