"""
Task
You need to return a string that looks like a diamond shape when printed on the screen, using asterisk (*) characters. Trailing spaces should be removed, and every line must be terminated with a newline character (\n).

Return null/nil/None/... if the input is an even number or negative, as it is not possible to print a diamond of even or negative size.


"""

n = 7


def diamond(n):

    if n < 0 or n % 2 == 0:
        return None

    diamond_string = ""
    n_f = n + 1

    range_list = list(range(1, n_f))
    range_list_reverse = range_list[::-1]

    for diamond in range_list:
        if diamond % 2 != 0:
            if diamond == n:
                diamond_item = (diamond * "*") + "\n"
            else:
                diamond_stars = (diamond * "*") + "\n"
                diamond_spaces = (((range_list[-1] - diamond) // 2) * " ")
                diamond_item = diamond_spaces + diamond_stars
            diamond_string += diamond_item

    for diamond in range_list_reverse[1:]:
        if diamond % 2 != 0:
            diamond_stars = (diamond * "*") + "\n"
            diamond_spaces = (((range_list[-1] - diamond) // 2) * " ")
            diamond_item = diamond_spaces + diamond_stars
            diamond_string += diamond_item

    return diamond_string


print(diamond(n))
