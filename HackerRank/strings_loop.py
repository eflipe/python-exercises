n = int(input())


for i in range(n):
    s = input()
    even = ''
    odd = ''
    for l in range(len(s)):
        if l % 2 == 0:
            even += s[l]
        else:
            odd += s[l]
    print(even + ' ' + odd)
