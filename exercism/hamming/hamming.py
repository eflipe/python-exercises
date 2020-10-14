# strand_a = 'GAGCCTACTAACGGGAT'
# strand_b = 'CATCGTAATGACGGCCT'
# strand_c = "ATA"
# strand_d = "ATAT"


def distance(strand_a, strand_b):

    if len(strand_a) != len(strand_b):
        raise ValueError("Different lengths: {} != {}.".format(len(strand_a), len(strand_b)))

    hamming_distance = 0

    for i, j in zip(strand_a, strand_b):
        if i != j:
            hamming_distance += 1

    return hamming_distance


# distance(strand_c, strand_d)
