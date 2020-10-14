seq_1 = ['Tokyo', 'London', 'Rome', 'Donlon', 'Kyoto', 'Paris', 'Okyot']
seq_2 = ['Rome', 'Rome', 'Rome', 'Donlon', 'London']
seq_3 = ['Nvvcoraeu', 'Rvancouve']


def group_cities(seq):
    seq_list = []

    def rotate(city):
        for r in range(len(city)):
            return (city[r:] + city[:r]).lower()

    for city_1 in seq:
        print(city_1)
        # city_1_sorted = (city_1[-1] + city_1[:-1]).lower()
        city_list = []
        for city_2 in seq:
            # city_2_sorted = (city_2[-1] + city_2[:-1]).lower()
            print(city_2)
            print(city_1_sorted)
            print(city_2_sorted)
            if city_1_sorted == city_2_sorted and city_2 not in city_list:
                city_list.append(city_2)
                print(city_list)

        city_list_sorted = sorted(city_list)

        if city_list_sorted not in seq_list and city_list not in seq_list:
            seq_list.append(city_list_sorted)

    seq_list.sort()
    seq_list_sorted = sorted(seq_list, key=len, reverse=True)
    print(seq_list_sorted)


group_cities(seq_1)
