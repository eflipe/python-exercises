def is_armstrong_number(number):
    str_number = str(number)
    len_num = len(str_number)
    armstrong = 0
    for num in str_number:
        armstrong += int(num) ** int(len_num)
    if armstrong == number:
        return True
    else:
        return False


"""
Otra solucion:
def is_armstrong(number):
    exp = len(str(number))
    return number == sum((int(a) ** exp for a in str(number)))

"""
