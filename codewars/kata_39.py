# https://www.codewars.com/kata/5663f5305102699bad000056/train/python

def mxdiflg(array_1, array_2):
    if not array_1 or not array_2:
        return -1

    min_len_array_1 = len(min(array_1, key=len))
    max_len_array_1 = len(max(array_1, key=len))
    min_len_array_2 = len(min(array_2, key=len))
    max_len_array_2 = len(max(array_2, key=len))

    max_len_diff_1 = abs(max_len_array_1 - min_len_array_2)

    max_len_diff_2 = abs(max_len_array_2 - min_len_array_1)


    return max(max_len_diff_1, max_len_diff_2)



# otra
def mxdiflg(a1, a2):
    mx = -1
    for x in a1:
        for y in a2:
            diff = abs(len(x) - len(y))
            if (diff > mx):
                mx = diff
    return mx

def mxdiflg(a1, a2):
    if not a1 or not a2: return -1

    print(max(a1, key=len))
    print(min(a1, key=len))

    max_a1, min_a1 = len(max(a1, key=len)), len(min(a1, key=len))
    max_a2, min_a2 = len(max(a2, key=len)), len(min(a2, key=len))

    return max(abs(max_a1 - min_a2), abs(max_a2 - min_a1))


if __name__ == "__main__":
    s1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]  # "YourNameHere"
    s2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
    s3 = ['vvcclllhhhyycvyyvvvyy', 'sppnnnxx', 'bbbiitttudddssiiiwwwrrriii', 'aaarmm']
    s4 = ['xxxxx', 'cccmuuyyyy', 'mq', 'mmmqqqvvvnnnyyl', 'ss', 'yyyzzzzzsss', 'uuz', 'moooyyy']
    output = mxdiflg(s1, s2) # 24
    print(output)
