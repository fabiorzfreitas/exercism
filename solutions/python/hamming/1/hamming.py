def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    hamming = 0
    for index, letter in enumerate(strand_a):
        if letter != strand_b[index]:
            hamming += 1
    return hamming
