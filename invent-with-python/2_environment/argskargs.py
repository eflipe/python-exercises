"""
an example by creating a product() function that takes any number of arguments and multiplies them together

"""

def product(*args):
    result = 1
        for num in args:
            result *= num
        return result


"""
args is just a regular Python tuple containing all the positional arguments
Technically, you can name this parameter anything, as long as it begins with the star (*), but it’s usually named args by convention.
"""

# map
mapObj = map(lambda n: str(n), [8, 16, 18, 19, 12, 1, 6, 7])
list(mapObj)

# filter
filterObj = filter(lambda n: n % 2 == 0, [8, 16, 18, 19, 12, 1, 6, 7])
list(filterObj)

"""
But the map() and filter() functions are outdated ways to create mapped
or filtered lists in Python. Instead, you can now create them with list comprehensions. List comprehensions not only free you from writing out a lambda function, but are also faster than map() and filter().
"""
# Here we replicate the map() function example using a list comprehension:
[str(n) for n in [8, 16, 18, 19, 12, 1, 6, 7]]

[n for n in [8, 16, 18, 19, 12, 1, 6, 7] if n % 2 == 0]
