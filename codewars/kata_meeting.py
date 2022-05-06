'''
John has invited some friends. His list is:

s = "Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill";

Could you make a program that

    makes this string uppercase
    gives it sorted in alphabetical order by last name.

When the last names are the same, sort them by first name. Last name and first name of a guest come in the result between parentheses separated by a comma.

So the result of function meeting(s) will be:

"(CORWILL, ALFRED)(CORWILL, FRED)(CORWILL, RAPHAEL)(CORWILL, WILFRED)(TORNBULL, BARNEY)(TORNBULL, BETTY)(TORNBULL, BJON)"

It can happen that in two distinct families with the same family name two people have the same first name too.

'''



def meeting(s):
    template = '({}, {});'
    str_list = ''
    start_index = 0
    mid_index = 0
    end_index = 0
    s += ';'
    print(s)
    for index, let in enumerate(s):
        if let == ':':
            mid_index = index
        if let == ';':
            end_index = index

        if mid_index and end_index:
            name = s[start_index:mid_index]
            print('name ----->', name)
            surname = s[mid_index + 1:end_index]
            print('surname --->', surname)
            start_index = end_index + 1
            mid_index = 0
            end_index = 0
            str_list += template.format(surname,name).upper()

    print('str list --->', str_list)
    string_split = str_list.split(';')
    string_split.sort()
    print("STR SPLIT --->", string_split)
    string_join = ''.join(string_split)
    print("STR JOIN --->", string_join)
    return string_join


if __name__ == "__main__":
    s = "Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"
    output = meeting(s)
    # print(output)


# otras soluciones:

def meeting(s):
  s = s.upper()
  s = s.split(';')
  array = []
  string = ""
  for i in s:
    i = i.split(':')
    string = '('+i[1]+', '+i[0]+')'
    array.append(string)
  array.sort()
  output = ""
  for j in array:
    output += j
  return output

def meeting(s):
    s = s.split(";")
    s.sort()
    x = []
    for i in s:
        first = i.split(":")[0]
        last = i.split(":")[1]
        x.append(str("(" + last.upper() + ", " + first.upper() + ")"))
    x.sort()

    return ''.join(x)
