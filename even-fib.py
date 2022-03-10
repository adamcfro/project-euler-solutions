def even_fib():
    '''This function finds the even numbers in the Fibonacci sequence and finds their total sum.'''
    a, b = 0, 1
    total = 0
    for num in range(1, 4000):
        if num % 2 == 0:
            total += num
            a, b = b, a + b
    return total


print(even_fib())