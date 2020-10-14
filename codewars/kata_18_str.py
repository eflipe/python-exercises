seq = ['Tokyo', 'London', 'Rome', 'Donlon', 'Kyoto', 'Paris', 'Okyot']
# out: [['Kyoto', 'Okyot', 'Tokyo'], ['Donlon', 'London'], ['Paris'], ['Rome']])
seq_2 = ['Rome', 'Rome', 'Rome', 'Donlon', 'London']
seq_3 = ['Nvvcoraeu', 'Rvancouve']

def group_cities(seq):

    seq_out = []

    for city_1 in seq:
        item_sorted = sorted(city_1.lower())
        city_list = []
        for city_2 in seq:
            city_sorted = sorted(city_2.lower())
            print(city_2)
            print(city_sorted)
            if item_sorted == city_sorted and city_2 not in city_list:
                city_list.append(city_2)
                print(city_list)

        city_list_sorted = sorted(city_list)
        if city_list_sorted not in seq_out and city_list not in seq_out:
            seq_out.append(city_list_sorted)
    seq_out.sort()
    seq_out_sorted = sorted(seq_out, key=len, reverse=True)
    print(seq_out_sorted)


group_cities(seq_3)
