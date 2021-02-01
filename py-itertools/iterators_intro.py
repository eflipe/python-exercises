# class-based iterators
# paso a paso: https://dbader.org/blog/python-iterators
# Objects that support the __iter__ and __next__ dunder methods automatically work with for-in loops.


class RepeaterIterator:
    def __init__(self, source):
        self.source = source

    def __next__(self):
        return self.source.value


class Repeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self): # helper class
        return RepeaterIterator(self)


repeater = Repeater('Hello')
for item in repeater:
    pass
    # print(item)


repeater = Repeater('Hello')

iterator = repeater.__iter__()
# while True:
#     item = iterator.__next__()
    # print(item)

class Repeater_2:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        return self.value

class BoundedRepeater:
    def __init__(self, value, max_repeats):
        self.value = value
        self.max_repeats = max_repeats
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_repeats:
            raise StopIteration
        self.count += 1
        return self.value

 repeater = BoundedRepeater('Hello', 3)
 for item in repeater:
        print(item)
