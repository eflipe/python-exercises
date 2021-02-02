# https://stackabuse.com/introduction-to-pythons-collections-module/
"""
The Counter() function in collections module takes an iterable or a mapping as the argument and returns a Dictionary. In this dictionary, a key is an element in the iterable or the mapping and value is the number of times that element exists in the iterable or the mapping.
"""
from collections import Counter, defaultdict, OrderedDict, deque, ChainMap, namedtuple

# crear Counter objects

cnt = Counter()

# You can pass an iterable (list) to Counter() function to create a counter object.

list = [1,2,3,4,1,2,6,7,3,8,1]
cnt = Counter(list)
print(cnt)
# You can access any counter item with its key as shown below:
print(cnt[1])
"""
cnt is an object of Counter class which is a subclass of dict. So it has all the methods of dict class.

Apart from that, Counter has three additional functions:

Elements
Most_common([n])
Subtract([interable-or-mapping])

"""
# elements() function. It returns a list containing all the elements in the Counter object.
cnt_2 = Counter({1:3, 2:4}) # le pasamos un dict}
cnt_element = cnt.elements()
print(cnt_element)
print(tuple(cnt_2.elements()))

# most_common()
# The Counter() function returns a dictionary which is unordered. You can sort it according to the number of counts in each element using most_common() function of the Counter object.
list = [1,2,3,4,1,2,6,7,3,8,1]
cnt = Counter(list)
print(cnt.most_common())

# subtract() takes iterable (list) or a mapping (dictionary) as an argument and deducts elements count using that argument
cnt = Counter({1:3,2:4})
deduct = {1:1, 2:2}
cnt.subtract(deduct)
print(cnt)

# defaultdict
# works exactly like a python dictionary, except for it does not throw KeyError when you try to access a non-existent key.
# Instead, it initializes the key with the element of the data type that you pass as an argument at the creation of defaultdict. The data type is called default_factory.
nums = defaultdict(int)
nums['one'] = 1
nums['two'] = 2
print(nums['three'])

# OrderedDict
# OrderedDict is a dictionary where keys maintain the order in which they are inserted, which means if you change the value of a key later, it will not change the position of the key.
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
print(od)
list = ["a","c","c","a","b","a","a","b","c"]
cnt = Counter(list)
od = OrderedDict(cnt.most_common())
for key, value in od.items():
    print(key, value)

# deque is a list optimized for inserting and removing items
list = ["a","b","c"]
deq = deque(list)
print(deq)
"""
You can easily insert an element to the deq we created at either of the ends. To add an element to the right of the deque, you have to use append() method.

If you want to add an element to the start of the deque, you have to use appendleft() method.

To remove an element from the right end, you can use pop() function and to remove an element from left, you can use popleft().
If you want to remove all elements from a deque, you can use clear() function.
"""
deq.append("d")
deq.appendleft("e")
print(deq)
deq.pop()
deq.popleft()
print(deq)
list = ["a","b","c"]
deq = deque(list)
print(deq)
print(deq.clear())

#  count(x) function. You have to specify the element for which you need to find the count, as the argument.
list = ["a","b","c"]
deq = deque(list)
print(deq.count("a"))

# ChainMap is used to combine several dictionaries or mappings. It returns a list of dictionaries.
dict1 = { 'a' : 1, 'b' : 2 }
dict2 = { 'c' : 3, 'b' : 4 }
chain_map = ChainMap(dict1, dict2)
print(chain_map.maps)
print(chain_map['c'])
dict2['c'] = 5
print(chain_map.maps)
# You can access the keys of a ChainMap with keys() function. Similarly, you can access the values of elements with values() function, as shown below:
dict1 = { 'a' : 1, 'b' : 2 }
dict2 = { 'c' : 3, 'b' : 4 }
chain_map = ChainMap(dict1, dict2)
print (list(chain_map.keys()))
print (list(chain_map.values()))
"""
Notice that the value of the key 'b' in the output is the value of key 'b' in dict1. As a rule of thumb, when one key appears in more than one associated dictionaries, ChainMap takes the value for that key from the first dictionary.
"""
# If you want to add a new dictionary to an existing ChainMap, use new_child() function. It creates a new ChainMap with the newly added dictionary.
dict3 = {'e':5, 'f':6}
new_chain_map = chain_map.new_child(dict3)
print(new_chain_map)

# namedtuple() returns a tuple with names for each position in the tuple.
"""
One of the biggest problems with ordinary tuples is that you have to remember the index of each field of a tuple object. This is obviously difficult. The namedtuple was introduced to solve this problem.
"""
Student = namedtuple('Student', 'fname, lname, age')
s1 = Student('John', 'Clarke', '13')
print(s1.fname)

# Creating a namedtuple Using List
# The namedtuple() function requires each value to be passed to it separately. Instead, you can use _make() to create a namedtuple instance with a list.
s2 = Student._make(['Adam','joe','18'])
print(s2)
