def splitpart(url_value):
    return (' ').join(url_value.split(':')[-1].split('_')).capitalize()


print(splitpart(ex_3))
