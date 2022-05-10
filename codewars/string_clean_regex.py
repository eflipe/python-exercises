'''
Link al Kata: https://www.codewars.com/kata/57e1e61ba396b3727c000251

Your harried co-workers are looking to you for a solution to take
this garbled text and remove all of the numbers. Your program will take in a string and clean out all numeric characters, and return a string with spacing and special characters ~#$%^&!@*():;"'.,? all intact.

'''
import re



def string_clean(s):
    """
    Function will return the cleaned string
    """
    clean_string_regex = re.compile(r'\d')
    cleaned_string = clean_string_regex.sub('', s)
    print("str --->", cleaned_string)
    return cleaned_string


if __name__ == '__main__':
    test_1 = "123456789"  # ""
    test_2 = "(E3at m2e2!!)"  # (Eat me!!)
    test_3 = "Dsa32 cdsc34232 csa!!! 1I 4Am cool!"  # "Dsa cdsc csa!!! I Am cool!"
    output = string_clean(test_3)


# otra solucion copada
def string_clean(s):
    import re
    return ''.join(re.findall('\D',s))
