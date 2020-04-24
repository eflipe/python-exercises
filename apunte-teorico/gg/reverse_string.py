# https://www.geeksforgeeks.org/reverse-string-python-5-different-ways/


def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str
# otra
# Function to reverse a string
def reverse(string):
    string = string[::-1]
    return string
