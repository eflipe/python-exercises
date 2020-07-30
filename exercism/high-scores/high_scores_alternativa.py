lista = [1, 14, 22, 5, 9]
scores_1 = [70]


def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    return sorted(scores, reverse=True)[:3]
# sorted(scores)[:-4:-1]


print(latest(lista))
print(personal_best(lista))
print(personal_top_three(lista))
