n = int(input())
name_number = []
names = []
for i in range(n):
    queries = input()
    name_number.append(queries.split())

for i in range(n):
    query_name = input()
    names.append(query_name)

for i in range(n):
    if name_number[i][0] == names[i]:
        print(f'{name_number[i][0]}={name_number[i][1]}')
    else:
        print('Not found')

n = int(input())

name_number = dict(input().split() for i in range(n))


for i in range(n):
    names = input()
    if names in name_number:
        print(f'{names}={name_number[names]}')
    else:
        print('Not found')
# otra

#number of entries in phonebook
n = int(input().strip())
phoneBook = {}

#assign in phoneBook
for i in range(n):
    name, num = input().strip().split(' ')
    phoneBook[name] = num

#query phoneBook while there is input, exit when EOF
while(True):
    try:
        qName = input().strip()
        if qName in phoneBook:
            print('{}={}'.format(qName, phoneBook[qName]))
        else:
            print('Not found')
    except EOFError:
        break
# otra
import sys
n = input()
name_numbers = [raw_input().split() for _ in range(n)]
phone_book = {k: v for k,v in name_numbers}
ls = map(lambda x: x.strip(),sys.stdin.readlines())
for name in ls:
    if name in phone_book:
        print('%s=%s' % (name, phone_book[name]))
    else:
        print('Not found')

# otra
from sys import stdin

if __name__ == "__main__":
    lines = stdin.read().splitlines()

    n = int( lines[0] )
    phoneBook = dict( i.split() for i in lines[1:n+1] )

    print( "\n".join(["{0:}={1:}".format(i, phoneBook[i]) if i in phoneBook else "Not found" for i in lines[n+1:] ]) )

#---------
n = int(input())

name_number = dict(input().split() for i in range(n))


while True:
    try:
        names = input()
        if names in name_number:
            print(f'{names}={name_number[names]}')
        else:
            print('Not found')
    except:
        break


# La final:

import sys

n = int(input())

name_number = dict(input().split() for i in range(n))

names = [name.strip() for name in sys.stdin.readlines()]

for name in names:
    if name in name_number:
        print(f'{name}={name_number[name]}')
    else:
        print('Not found')
