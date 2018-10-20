def mult_3and5():
    '''This function takes numbers between 1 and 1000 and sums all numbers that are evenly divisible by 3 or 5.'''
    total = 0
    for num in range(1, 1000):
        if num % 3 == 0 or num % 5 == 0:
            total += num
    return total


print(mult_3and5())