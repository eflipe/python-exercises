# Replace all items: https://www.codewars.com/kata/57ae18c6e298a7a6d5000c7a/train/python
obj = "Hello World"
find = 'o'
replace = '0'

obj_1 = [1, 2, 1, 2, 3]
find_1 = 1
replace_1 = 2


def replace_all(obj, find, replace):
    if obj:
        new_list = list(obj)

        for index, item in enumerate(new_list.copy()):
            if item == find:
                new_list.remove(item)
                new_list.insert(index, replace)

        if isinstance(new_list[0], str):
            obj = ('').join(new_list)
        else:
            obj = new_list
    return obj


print(replace_all(obj_1, find_1, replace_1))

def replace_all(obj, find, replace):
  if isinstance(obj, str):
    return obj.replace(find, replace)
  elif isinstance(obj, list):
    return [x if x != find else replace for x in obj]


def replace_all(obj, find, replace):
    result = [el if el != find else replace for el in obj]
    return ''.join(result) if isinstance(obj, str) else result

def replace_all(obj, find, replace):
    if type(obj) is str:
        return obj.replace(find, replace)
    if type(obj) is list:
        for index,value in enumerate(obj):
            if value == find:
                obj[index] = replace
    return obj

print(replace_all(obj, find, replace))
