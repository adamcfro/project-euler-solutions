def lar_pal_pro():
    '''This function returns the largest palindrome made from the product of two 3-digit numbers.'''
    i = 999
    j = 999
    palindrome = False
    while not palindrome:
        string = str(i * j)
        if string[::] == string[::-1]:
            # palindrome = True
            return int(string)
        else:
            i -= 1


print(lar_pal_pro())