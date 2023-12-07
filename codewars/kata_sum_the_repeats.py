# Write a function that takes a list comprised of other lists of 
# integers and returns the sum of all numbers that appear in two or more lists in the input list. 
# Now that might have sounded confusing, it isn't:

# repeat_sum([[1, 2, 3],[2, 8, 9],[7, 123, 8]])
# >>> sum of [2, 8]
# return 10

# repeat_sum([[1], [2], [3, 4, 4, 4], [123456789]])
# >>> sum of []
# return 0

# repeat_sum([[1, 8, 8], [8, 8, 8], [8, 8, 8, 1]])
# sum of [1,8]
# return 9

from collections import Counter

list_1 = [[1, 2, 3],[2, 8, 9],[7, 123, 8]]
list_2 = [[1], [2], [3, 4, 4, 4], [123456789]]
list_3 = [[1, 8, 8], [8, 8, 8], [8, 8, 8, 1]]
list_4 = [[3, 6, 4], [7, 4], [4, 2]]


def repeat_sum(lst):
    # Flatten the input list
    flattened_list = [element for sublist in lst for element in set(sublist)]
    print(flattened_list)
    unique_list = list()
    for elem in set(flattened_list):
        if flattened_list.count(elem) > 1:
            unique_list.append(elem)
    
    return sum(unique_list)        
    
    # return sum(n for n in set(flattened_list) if flattened_list.count(n) > 1)

    # # Count the occurrences of each element
    # element_count = Counter(flattened_list)

    # # Create a list of repeated numbers
    # repeated_numbers = [element for element, count in element_count.items() if count > 1]
    # print(repeated_numbers)

    
    # # Calculate the sum of repeated numbers, if there is more than one repeated number
    # if len(repeated_numbers) > 1:
    #     sum_of_repeated_numbers = sum(repeated_numbers)
    # else:
    #     # If there is only one or no repeated numbers, set the sum to an empty list
    #     sum_of_repeated_numbers = []

    # return sum_of_repeated_numbers


print(repeat_sum(list_3))

