"""
Basically the * in this case is an instruction to 'unpack' the list,
which means that instead of providing
the list's elements grouped up like a list,
i.e. like [2, 4, 6], it pulls each of
the elements out and presents it individually,
so that instead you just get 2 4 6.
The net effect of which is that the
elements in the list are output
with a different format by the print
statement, one of which is accepted as
the correct answer, and the other isn't.
"""

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))


    print(*reversed(arr))




# Otra con map()
"""
print(" ".join(map(str, arr[::-1])))


Let's start from the Inside of map function,
the arr[::-1] will reverse the List
from [1, 2, 3, 4] to [4, 3, 2, 1] .
Now map takes a Function and a sequence.
So you have to convert your List to string
data type to perform join operation.
So after that you would be
having ['4', '3', '2', '1'] as a
str Now you have to Join each other
with a space in between,
hence you use " ".join(blahblah) .Therefore, you get output.
"""

#otra
print(' '.join(str(x) for x in arr[::-1]))

#otra
print(*input().split()[::-1])

#otra
print(*arr[::-1])
