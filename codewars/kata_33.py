def arrange(s):
    t = []
    s_list = s.copy()

    for element in range(len(s_list)):
        print("S list", s_list)
        if len(s_list) > 1:
            item_t_0 = s_list.pop(0)
            item_t_1 = s_list.pop(-1)
            t.append(item_t_0)
            t.append(item_t_1)
            s_list.reverse()
            print("S list", s_list)
            print("T list", t)
        if len(s_list) == 1:
            t.append(s_list[0])
            break

    print(s)
    print(t)
    return t

def arrange_while(s):
    t = []
    s_list = s.copy()

    while s_list:
        print("S list", s_list)
        if len(s_list) > 1:
            item_t_0 = s_list.pop(0)
            item_t_1 = s_list.pop(-1)
            t.append(item_t_0)
            t.append(item_t_1)
            s_list.reverse()
            print("S list", s_list)
            print("T list", t)
        if len(s_list) == 1:
            t.append(s_list[0])
            break

    print(s)
    print(t)
    return t

def arrange(s):
    t = []
    s_list = s.copy()
    flag = True

    while s_list:
        try:
            item_t_0 = s_list.pop(0)
            item_t_1 = s_list.pop(-1)
            if flag:
                t.append(item_t_0)
                t.append(item_t_1)
                flag = False
            else:
                t.append(item_t_1)
                t.append(item_t_0)
                flag = True

        except Exception as e:
            print(e)
            t.append(item_t_0)

    return t

def arrange(s):
    t = []
    s_list = s.copy()
    len_s = len(s)
    index = 0
    flag = True

    while len_s > len(t):
        print("S", len_s)
        print("T", len(t))
        item_t_0 = s[index]
        item_t_1 = s[-(index + 1)]
        if index % 2 == 0:
            print("t_0_t", item_t_0)
            print("t_1_t", item_t_1)
            if item_t_0 == item_t_1:
                print("t_0_difff", item_t_0)
                print("t_1_difff", item_t_1)
                t.append(item_t_0)
                break
            t.append(item_t_0)
            t.append(item_t_1)
        elif index % 2 != 0:
            print(len_s)
            print("t_0_f", item_t_0)
            print("t_1_f", item_t_1)
            if item_t_0 == item_t_1:
                print("t_0_difff", item_t_0)
                print("t_1_difff", item_t_1)
                t.append(item_t_1)
                break

            t.append(item_t_1)
            t.append(item_t_0)


        index += 1




    return t

s = [9, 7, -2, 8, 5, -3, 6, 5, 1]
# arrange(s)
arrange_while(s)
