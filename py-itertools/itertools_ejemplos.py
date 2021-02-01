from itertools import *
# https://realpython.com/python-itertools/

iter_items_1 = [1, 2, 3]
iter_items_2 = ['a', 'b', 'c']

iter_chain = ''
for i in chain([1, 2, 3], ['a', 'b', 'c']):
    iter_chain += str(i) + ' '
    print(i, end=' ')
print(iter_chain)
print(type(iter_chain))

#zip: devuelve una tupla
for i in zip(iter_items_1, iter_items_2):
    print(i)

#zip_longest: sigue iterando
r1 = range(3)
r2 = range(2)

print('zip stops early:')
print(list(zip(r1, r2)))

r1 = range(3)
r2 = range(2)

print('\nzip_longest processes all of the values:')

print(list(zip_longest(r1, r2)))

#By default, zip_longest() substitutes None for any missing values. Use the fillvalue argument to use a different substitute value.
print(list(zip_longest(r1, r2, fillvalue="Fin")))

#islice() function returns an iterator which returns selected items from the input iterator, by index.
print('Stop at 5:')
for i in islice(range(100), 5):
    print(i, end=' ')
print('\n')

print('Start at 5, Stop at 10:')
for i in islice(range(100), 5, 10):
    print(i, end=' ')
print('\n')

print('By tens to 100:')
for i in islice(range(100), 0, 100, 10):
    print(i, end=' ')
print('\n')

# map:  map() function returns an iterator that calls a function on the values in the input iterators, and returns the results. It stops when any input iterator is exhausted.
def times_two(x):
    return 2 * x


def multiply(x, y):
    return (x, y, x * y)


print('Doubles:')
for i in map(times_two, range(5)):
    print(i)

print('\nMultiples:')
r1 = range(5)
r2 = range(5, 10)
for i in map(multiply, r1, r2):
    print('{:d} * {:d} = {:d}'.format(*i))

print('\nStopping:')
r1 = range(5)
r2 = range(2)
for i in map(multiply, r1, r2):
    print(i)

# count() function returns an iterator that produces consecutive integers, indefinitely.
for i in zip(count(2), ['a', 'b', 'c']):
    print(i)

# cycle() function returns an iterator that repeats the contents of the arguments it is given indefinitely.
for i in zip(range(7), cycle(['a', 'b', 'c'])):
    print(i)

# repeat() function returns an iterator that produces the same value each time it is accessed.
for i in repeat('over-and-over', 5):
    print(i)

# combine repeat() with zip() or map() when invariant values need to be included with the values from the other iterators.
for i, s in zip(count(), repeat('over-and-over', 5)):
    print(i, s)

# Filtering
# dropwhile() function returns an iterator that produces elements of the input iterator after a condition becomes False for the first time.
# does not filter every item of the input; after the condition is false the first time, all of the remaining items in the input are returned.
def should_drop(x):
    print('Testing:', x)
    return x < 1


for i in dropwhile(should_drop, [-1, 0, 1, 2, -2]):
    print('Yielding:', i)

# takewhile(). It returns an iterator that returns items from the input iterator as long as the test function returns true.
def should_take(x):
    print('Testing:', x)
    return x < 2


for i in takewhile(should_take, [-1, 0, 1, 2, -2]):
    print('Yielding:', i)

# filter() returns an iterator that includes only items for which the test function returns true.
# is different from dropwhile() and takewhile() in that every item is tested before it is returned.
def check_item(x):
    print('Testing:', x)
    return x < 1


for i in filter(check_item, [-1, 0, 1, 2, -2]):
    print('Yielding:', i)

# compress() offers another way to filter the contents of an iterable. Instead of calling a function, it uses the values in another iterable to indicate when to accept a value and when to ignore it.
every_third = cycle([False, False, True])
data = range(1, 10)

for i in compress(data, every_third):
    print(i, end=' ')
print()
# groupby() function returns an iterator that produces sets of values organized by a common key.
# accumulate() function processes the input iterable, passing the nth and n+1st item to a function and producing the return value instead of either input. The default function used to combine the two values adds them, so accumulate() can be used to produce the cumulative sum of a series of numerical inputs.
print(list(accumulate(range(5))))
print(list(accumulate('abcde')))

# compose
list(map(sum, zip([1, 2, 3], [4, 5, 6])))
'''
You have three $20 dollar bills, five $10 dollar bills, two $5 dollar bills, and five $1 dollar bills. How many ways can you make change for a $100 dollar bill?
'''

bills = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]

# A choice of k things from a set of n things is called a combination, and itertools has your back here. The itertools.combinations()
# itertools.combinations() function takes two arguments—an iterable inputs and a positive integer n—and produces an iterator over tuples of all combinations of n elements in inputs.
print(list(combinations(bills, 3)))

makes_100 = []
for n in range(1, len(bills) + 1):
    for combination in combinations(bills, n):
        if sum(combination) == 100:
            makes_100.append(combination)

print(makes_100)
print("LEN LIST", len(makes_100))
print("SET", set(makes_100))
set_makes_100 = set(makes_100)
print("SET LIST", len(set_makes_100))

# combinations_with_replacement()
# It works just like combinations(), accepting an iterable inputs and a positive integer n, and returns an iterator over n-tuples of elements from inputs. The difference is that combinations_with_replacement() allows elements to be repeated in the tuples it returns.
bills_2 = [50, 20, 10, 5]
make_50 = []
for n in range(1, 50):
    for combi in combinations_with_replacement(bills_2, n):
        if sum(combi) == 100:
            make_50.append(combi)

print(len(make_50))
print(make_50)

# permutations(), which accepts a single iterable and produces all possible permutations (rearrangements) of its elements:
