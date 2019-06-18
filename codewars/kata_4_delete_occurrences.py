'''
Task
Given a list lst and a number N, create a new list that contains
each number of lst at most N times without reordering.
For example if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2],
drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times,
and then take 3, which leads to [1,2,3,1,2,3].

Example
  delete_nth ([1,1,1,1],2) # return [1,1]

  delete_nth ([20,37,20,21],1) # return [20,37,21]
'''


lista = [1, 2, 3, 1, 2, 1, 2, 3]
lista_2 = [1, 1, 1, 1]
lista_3 = [20, 37, 20, 21]
lista_4 = [1, 1, 3, 3, 7, 2, 2, 2, 2]


def delete_nth(order, max_e):
    list = []
    for item in order:
        list.append(item)
        if list.count(item) > max_e:
            list.pop()

    return list


print(delete_nth(lista, 2))
"""
Otra soluciones:

def delete_nth(order,max_e):
    ans = []
    for o in order:
        if ans.count(o) < max_e: ans.append(o)
    return ans

def delete_nth(order,max_e):
    answer = []
    for x in order:
        if answer.count(x) < max_e:
            answer.append(x)

    return answer
"""
