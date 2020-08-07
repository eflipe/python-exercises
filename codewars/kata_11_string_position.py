

st = "Addison,Jayden,Sofia,Michael,Andrew,Benjamni,Lily,Benjamin"
we = [4, 2, 1, 4, 3, 2, 1, 2]
n = 4

st_2= "COLIN,AMANDBA,AMANDAB,CAROL,PauL,JOSEPH"
we_2= [1, 4, 4, 5, 2, 1]
n_2 = 4
import string as alpha

def rank(st, we, n):
    ranking = []
    str_names = st.split(',')

    if str == "":
        return "No participants"

    if n > len(str_names):
        return "Not enough participants"

    alpha_list = list(alpha.ascii_lowercase)

    for name_index in range(len(str_names)):
        points = 0
        print(f'{str_names[name_index]}, puntos parciales: {points}')
        for let_name in str_names[name_index]:
            for alpha_index in range(len(alpha_list)):
                if let_name.lower() == alpha_list[alpha_index]:
                    points += alpha_index + 1
                    print(f'Letra {let_name.lower()}, puntos: {alpha_index + 1}, puntos parciales: {points}')
        print(f'{str_names[name_index]}, puntos parciales: {points}')
        points += len(str_names[name_index])
        print(f'Len: {str_names[name_index]}')
        print(f'{str_names[name_index]}, puntos parciales: {points}')
        print(f'Multipli por {we[name_index]}')
        points = points * we[name_index]
        ranking.append(points)

    print(ranking)

    rank_sort = sorted(ranking, reverse=True)
    print(rank_sort)
    # max_rank = max(ranking)
    # index_max_rank = ranking.index(max(ranking))
    # print(max_rank)
    # print(index_max_rank)
    winner_rank = rank_sort[n-1]
    winner_index = ranking.index(winner_rank)
    winner = str_names[winner_index]
    print(winner)
    return winner




import string as alpha


def rank_2(st, we, n):
    ranking = []
    rank_sort_names = []
    rank_dict = {}
    st_names = st.split(',')

    if st == "":
        return "No participants"

    if n > len(st_names):
        return "Not enough participants"

    alpha_list = list(alpha.ascii_lowercase)

    for name_index in range(len(st_names)):
        points = 0

        for let_name in st_names[name_index]:
            for alpha_index in range(len(alpha_list)):
                if let_name.lower() == alpha_list[alpha_index]:
                    points += alpha_index + 1

        points += len(st_names[name_index])

        points = points * we[name_index]

        rank_dict[st_names[name_index]] = points

        # ranking.append(points)
        # rank_sort_points = sorted(ranking, reverse=True)
        # winner_index = ranking.index(winner_rank)
        # rank_sort_names.append()
        # print(f'Progress: {rank_sort_points}')
        # rank_sort_names[name_index]

    # rank_sort = sorted(ranking, reverse=True)

    #winner_rank = rank_sort[n-1]
    # winner_index = ranking.index(winner_rank)
    # print(rank_sort)
    # winner = st_names[winner_index]
    # print(winner)
    print(rank_dict)
    sorted_rank_dict = list(sorted(rank_dict.items(), key=lambda kv: (-kv[1], kv[0])))
    print(sorted_rank_dict)
    # let_rank = alpha_list[n-1]
    # print(let_rank)
    winner_pt = sorted_rank_dict[n-1][0]
    # winner = sorted_rank_dict.items()[n-1]
    # winner = sorted_rank_dict.values().index(winner_pt)
    return winner_pt

print(rank_2(st_2, we_2, n_2))