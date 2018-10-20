# def ten_thousand_one_prime():
#     '''.'''
#     num = 13
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True



# print(ten_thousand_one_prime())


# # notes: right now the function only tells whether num is prime


# def ten_thousand_one_prime():
#     lst = range(2, 13)
#     for i, num in enumerate(lst):
#         if num % 



# print(ten_thousand_one_prime())



import time
 
# function to factor a given positive integer n
def is_prime(n):
    # look for factors of 2 first
    if n % 2 == 0: return False
    # now look for odd factors
    p = 3
    while p < n**0.5+1:
        if n % p == 0: return False
        p += 2
    return True
 
def nth_prime(n):
    prime = 2
    count = 1
    iter = 3
    while count < n:
        if is_prime(iter):
            prime = iter
            count += 1
        iter += 2
    return prime
 
start = time.time()
prime = nth_prime(10001)
elapsed = (time.time() - start)
 
print(f"found {prime} in {elapsed} seconds")

