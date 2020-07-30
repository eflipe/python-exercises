# https://www.geeksforgeeks.org/python-program-check-string-palindrome-not/
# 1
def reverse(s):
    return s[::-1]

def isPalindrome(s):
    # Calling reverse function
    rev = reverse(s)

    # Checking if both string are equal or not
    if (s == rev):
        return True
    return False


# Driver code
s = "malayalam"
ans = isPalindrome(s)

if ans == 1:
    print("Yes")
else:
    print("No")

# 2: Iterative Method:
# function to check string is
# palindrome or not
def isPalindrome(str):

    # Run loop from 0 to len/2
    for i in xrange(0, len(str)/2):
        if str[i] != str[len(str)-i-1]:
            return False
    return True

# main function
s = "malayalam"
ans = isPalindrome(s)

if (ans):
    print("Yes")
else:
    print("No")

# 3:Method using inbuilt function to reverse a string: This method is contributed by Shariq Raza. In this method, predefined function ‘ ‘.join(reversed(string))
# function to check string is
# palindrome or not
def isPalindrome(s):

    # Using predefined function to
    # reverse to string print(s)
    rev = ''.join(reversed(s))

    # Checking if both string are
    # equal or not
    if (s == rev):
        return True
    return False

# main function
s = "malayalam"
ans = isPalindrome(s)

if (ans):
    print("Yes")
else:
    print("No")

# 4: usando una variable extra
# Python program to check
# if a string is palindrome
# or not

x = "malayalam"
w = ""
for i in x:
    w = i + w
    if (x==w):
        print("YES")
