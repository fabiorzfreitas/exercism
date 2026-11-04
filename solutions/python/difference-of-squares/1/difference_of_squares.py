def square_of_sum(number):
    sq_sum = []
    for i in range(number):
        sq_sum.append(i + 1)
    return sum(sq_sum) ** 2

def sum_of_squares(number):
    sum_sq = []
    for j in range(number):
        sum_sq.append((j + 1) ** 2)
    return sum(sum_sq)


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
