#number = 105
#number2 = 101
# number3 = 9

def convert(number):
    raindrops = []

    if number % 3 == 0:
        raindrops.append('Pling')

    if number % 5 == 0:
        raindrops.append('Plang')

    if number % 7 == 0:
        raindrops.append('Plong')

    if raindrops:
        return ('').join(raindrops)
    else:
        return str(number)


# print(convert(number3))
