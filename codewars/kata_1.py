
def count_sheep(n):
    mensaje3 = ""
    for n in range(n):
        mensaje2 = ''
        mensaje2 = str(n+1) + " sheep..."

        mensaje3 += mensaje2
    return mensaje3


print(count_sheep(4))


def count_sheep(n):
    empty_string = ""
    final_string = ""
    for n in range(n):
        empty_string = ""
        empty_string = str(n+1) + " sheep..."

        final_string += empty_string
        # mensaje = "'" + str(n+1) + " sheep..." + "'"

    return final_string
