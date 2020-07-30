'''
We need a method in the List Class that may count
specific digits from a given list of integers.
This marked digits will be given in a second list.
The method .count_spec_digits()/.countSpecDigits()
will accept two arguments, a list of an uncertain amount
of integers integers_lists/integersLists
(and of an uncertain amount of digits, too)
and a second list, digits_list/digitsList that has
the specific digits to count which length cannot
be be longer than 10 (It's obvious, we've got ten digits).
The method will output a list of tuples,
each tuple having two elements, the first one will be
a digit to count, and second one, its corresponding
total frequency in all the integers of the first list.
This list of tuples should be ordered with
the same order that the digits have in digitsList

'''
from collections import Counter

integers_list = [1, 1, 2 ,3 ,1 ,2 ,3 ,4]
digits_list = [1, 3]

integers_list_2 = [-18, -31, 81, -19, 111, -888]
digits_list_2 = [1, 8, 4]

s = "".join(str(i) for i in integers_list_2)
print(s)
print([(dig, s.count(str(dig))) for dig in digits_list_2])




# # intersecption
# interList = [x for x in str(absList) if x in str(digits_list_2)]
# # list(set(integers_list) & set(digits_list))
# print(interList)
#
# counter = Counter(interList)
# # miscellaneous examples
# counterItems = counter.items()   # dict_items([('a', 3), ('b', 3), ('c', 0)])
#
# dictList = []
# for key, value in counterItems:
#     dictList.append((key, value))
#
# print(dictList)
# def filterInt(integers_list, digits_list):
#
#     if(integers_list in digits_list):
#         print(digits_list)
#         return True
#     else:
#         return False
#
#
# filterInt(integers_list, digits_list)
#
# filteredVowels = filter(filterVowels, letters)
#
# print('The filtered vowels are:')
# for vowel in filteredVowels:
#     print(vowel)

# class List(object):
#     def count_spec_digits(self, integers_list, digits_list):
#         # your code here
#         return [(,), (,), ..,(,)]
#
#
# l = List()
# l.count_spec_digits(integers_list, digits_list)
