seq_1 = ['Tokyo', 'London', 'Rome', 'Donlon', 'Kyoto', 'Paris', 'Okyot']
seq_2 = ['Rome', 'Rome', 'Rome', 'Donlon', 'London']
seq_3 = ['Nvvcoraeu', 'Rvancouve']


def group_cities(seq):
    seq_list = []
    for city_1 in seq:
        city_list = []
        print('City_1', city_1)
        for city_2 in seq:
            print('City_2', city_2)
            for r in range(len(city_1)):
                city_rotate = (city_1[r:] + city_1[:r]).lower()
                print(city_rotate)

                if city_rotate == city_2.lower() and city_2 not in city_list:
                    city_list.append(city_2)
                    print(city_list)

        city_list_sorted = sorted(city_list)
        if city_list_sorted not in seq_list and city_list not in seq_list:
            seq_list.append(city_list_sorted)
    seq_list.sort()
    seq_out_sorted = sorted(seq_list, key=len, reverse=True)
    print(seq_out_sorted)

group_cities(seq_2)
