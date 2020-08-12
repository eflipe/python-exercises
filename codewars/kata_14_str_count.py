city_1 = "Chicago"  # "c:**,h:*,i:*,a:*,g:*,o:*"
city_2 = "Bangkok"  # "b:*,a:*,n:*,g:*,k:**,o:*"
city_3 = "Las Vegas"  # "l:*,a:**,s:**,v:*,e:*,g:*"


def get_strings(city):

    city = city.lower().replace(' ', '')
    unique_city_list = []

    city_list = [f'{char}:{city.count(char) * "*"}' for char in city]

    for char in city_list:
        if char not in unique_city_list:
            unique_city_list.append(char)

    return ','.join(unique_city_list)


print(get_strings(city_3))

# otra

# from collections import Counter
#
#
# def get_strings(city):
#     return ",".join(f"{char}:{'*'*count}" for char, count in Counter(city.replace(" ", "").lower()).items())

#

#from collections import Counter
# def get_strings(city):
#     lst = []
#     for key, value in dict(Counter(city.replace(' ', '').lower())).items():
#         lst.append(key+':'+'*'*value)
#     return ','.join(lst)
