# initialize
a = []

# create the table (name, age, job)
a.append(["Nick", 30, "Doctor", 100])
a.append(["John", 8, "Student", 90])
a.append(["Paul", 22, "Car Dealer", 87])
a.append(["Mark", 66, "Retired", 5])

# sort the table by age
import operator
a.sort(key=operator.itemgetter(3))

# print the table
print(a)

a.sort(key=operator.itemgetter(1), reverse=True)
print(a)

'''
operator.itemgetter(n) constructs a callable
that assumes an iterable object (e.g. list, tuple, set)
as input, and fetches the n-th element out of it.

con lambda_

a.sort(key=lambda elem: elem[1])

con una funcion:

get_second_elem
def get_second_elem(iterable):
    return iterable[1]

a.sort(key=get_second_elem) #sorteame el item que te pido


The key= parameter of sort requires a key function (to be applied
to be objects to be sorted) rather than a single key
value and
that is just what operator.itemgetter(1) will give you:
A function that grabs the first item from a list-like object.
'''
