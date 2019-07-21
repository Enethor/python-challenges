# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


def sum_of_squares(lowest, highest):
    sum = 0
    for x in range(lowest, highest + 1):
        sum += (x*x)
    return sum


def square_of_sum(lowest, highest):
    sum = 0
    for x in range(lowest, highest + 1):
        sum += x
    return sum*sum


def difference(lowest, highest):
    square_sum = square_of_sum(lowest, highest)
    sum_squares = sum_of_squares(lowest, highest)
    print(square_sum - sum_squares)


difference(1, 100)
