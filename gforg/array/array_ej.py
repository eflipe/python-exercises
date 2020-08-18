#  array(data type, value list)
# Python code to demonstrate the working of
# array(), append(), insert()
# https://www.geeksforgeeks.org/array-python-set-1-introduction-functions/
# importing "array" for array operations
import array

# initializing array with array values
# initializes array with signed integers
arr = array.array('i', [1, 2, 3])

# printing original array
print(arr)
print(type(arr))
arr.append(4)
arr.insert(2, 5)

print("The new created array is : ")
for i in range(0, 5):

    print(arr[i], end=" ")
    print(type(i))

print("\r")

print("The datatype of array is : ")
print(arr.typecode)

# using itemsize to print itemsize of array
print("The itemsize of array is : ")
print(arr.itemsize)

# using buffer_info() to print buffer info. of array
print("The buffer info. of array is : ")
print(arr.buffer_info())

# using count() to count occurrences of 1 in array
print("The occurrences of 1 in array is : ")
print(arr.count(1))

# initializing list
li = [1, 2, 3]

# using fromlist() to append list at end of array
arr.fromlist(li)

# using tolist() to convert array into list
li2 = arr.tolist()

print("\r")

# printing the new list
print("The new list created is : ", end="")
for i in range(0, len(li2)):
    print(li2[i], end=" ")