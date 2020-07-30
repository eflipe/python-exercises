    n = int(input())
    number = []

while(n > 0):
    div = int(n/2);
    remainder = n%2;
    number.append(remainder)
    n = div

print(*reversed(number))

#otra

    n = int(input().strip())

numbers = str(bin(n)[2:]).split('0')
print(numbers)
lenghts = [len(num) for num in numbers]
print(lenghts)
print(max(lenghts))

# otra
n = int(input().strip())
print(max(map(len, bin(n)[2:].split("0")))

# otra
import sys
import math

n = int(input().strip())

# create an empty list to hold our binary numbers
binary_list = []

# fill the list with 1s and 0s from left to right using Base-Conversion Method (remainders of dividing by 2)
while True:
    if n > 1:
        if n % 2 == 0:
            binary_list.append(0)
        elif n % 2 != 0:
            binary_list.append(1)
    elif n == 1:
        binary_list.append(1)
        break
    elif n == 0:
        binary_list.append(0)
        break
    n = math.floor(n / 2)

# set a counter and a max variable
consec = 0
maximum = 0

# iterate through our list of 1s and 0s to find our max consecutive set of 1s
for i in binary_list:
    if i == 1:
        consec += 1
        if maximum <= consec:
            maximum = consec
        else:
            pass
    elif i == 0:
        consec = 0

print(maximum)
