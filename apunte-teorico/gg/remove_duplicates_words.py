# Given a sentence containing n words/strings. Remove all duplicates words/strings which are similar to each others
from collections import Counter

def remov_duplicates(input):

    # split input string separated by space
    input = input.split(" ")
    print(input)

    # joins two adjacent elements in iterable way
    # for i in range(0, len(input)):
    #     print(input[i])
    #     input[i] = "".join(input[i])


    # now create dictionary using counter method
    # which will have strings as key and their
    # frequencies as value
    UniqW = Counter(input)
    print(UniqW)

    # joins two adjacent elements in iterable way
    s = " ".join(UniqW.keys())
    print(s)

# Driver program
if __name__ == "__main__":
    input = 'Python is great and Java is also great'
    remov_duplicates(input)


# otra
# Program without using any external library
s = "Python is great and Java is also great"
l = s.split()
k = []
for i in l:

    # If condition is used to store unique string
    # in another list 'k'
    if (s.count(i)>1 and (i not in k)or s.count(i)==1):
        k.append(i)
print(' '.join(k)) 
