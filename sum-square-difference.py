def sum_square_difference():
    '''This function returns the difference between the sum of the squares and the square of the sum of the first one hundred natural numbers.'''
    i = 1
    sum_squares = 0
    square_sum = 0
    while i < 101:
        sum_squares += i * i
        square_sum += i
        i += 1
    return (square_sum * square_sum) - sum_squares


print(sum_square_difference())