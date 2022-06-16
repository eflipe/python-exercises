'''
Link: https://www.codewars.com/kata/585d8c8a28bc7403ea0000c3
There is an array of strings. All strings contains similar letters except one. Try to find it!

find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]) # => 'BbBb'
find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]) # => 'foo'

Strings may contain spaces. Spaces are not significant, only non-spaces symbols matters.
E.g. string that contains only spaces is like empty string.

It’s guaranteed that array contains more than 3 strings.

'''

string_1 = [ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ] # 'BbBb'
string_2 = [ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ] # => 'foo'
string_3 = [ '    ', 'a', '  ' ]


def find_uniq(arr):

    arr_to_string = ''.join(arr)
    unique_str = ''
    for item in arr:
        item_lower = item.lower()
        sorted_item = ''.join(sorted(item_lower))
        item_counter = arr_to_string.count(sorted_item)
        if item_counter == 1:
            unique_str = item


    return unique_str

# def find_uniq(arr):
#
#     arr_to_string = ''.join(arr).lower()
#     unique_str = ''
#     for index, item in enumerate(arr):
#         item = item.lower()
#         sorted_item = ''.join(sorted(item))
#         item_counter = arr_to_string.count(sorted_item)
#         if item_counter == 1:
#             unique_str = arr[index]
#
#
#     return unique_str

print(find_uniq(string_1))
