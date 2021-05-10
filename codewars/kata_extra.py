list_url = ['/es-es/']
#print(list_url)

ex_1 = '/es-es/'  # return nada


def splitpart(url_value):
    value_split = (' ').join(url_value.split('/')[-2].split('-')).capitalize()
    print(value_split)
    return value_split


print(splitpart(ex_1))
