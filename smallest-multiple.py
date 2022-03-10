def smallest_multiple():
    '''This program finds the smallest number than is evenly divisible by all of the numbers from 1 to 20.'''
    i = 1
    num = 1
    while i < 10:
        if num % i == 0:
            i += 1
        else:
            num += 1
            i = 1
    return num

print(smallest_multiple())



# notes: this program works but there is a faster way to compute. if need to get rid of multiples of unacceptable numbers