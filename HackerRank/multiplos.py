"""
Task
Given an integer, , print its first multiples. Each multiple (where ) should be printed
on a new line in the form: n x i = result
"""

n = 2

for i in range(1, 11):
    print(f'{n} X {i} = {n * i}')
