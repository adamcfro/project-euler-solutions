# noprimes = set(j for i in range(2, 8) for j in range(i*2, 50, i))

# primes = [x for x in range(2, 50) if x not in noprimes]

# print(primes)


def is_prime(n):
    '''Brute force test if n is prime by trial division'''
    if 2 < n < 4:
        return True
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
 
primes_under_100 = [p for p in range(2,101) if is_prime(p)]
print(primes_under_100)