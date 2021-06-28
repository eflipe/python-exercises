numbers_str ="899091939495" # "123567" # 4
numbers_list = list(numbers_str)
print(numbers_list)
numbers_sorted = sorted(numbers_list)
print(set(numbers_sorted))



def missing(s):
    for i in range(len(s) - 1):
        if (int(s[i]) + 1) != (int(s[i+1])):
            # print(s[i])
            # print(int(s[i]) + 1)
            pass

def missing(s):
    for length in range(1, len(s)//2 +1):

        position, num , miss  = length , int(s[:length]) + 1 , False
        while position < len(s):
            if s[position:].startswith(f"{num}"):
                position += len(str(num))
                num += 1
            elif s[position:].startswith(f"{num+1}") and not miss:
                miss = num
                position += len(str(num+1))
                num += 2
            else:
                miss = False
                break
        if miss : return miss
    return -1

if __name__ == '__main__':
    missing(numbers_str)
