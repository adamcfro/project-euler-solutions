num = 2 ** 1000

num = [int(i) for i in list(str(num))]

total = 0
for i in num:
    total += i

print(total)