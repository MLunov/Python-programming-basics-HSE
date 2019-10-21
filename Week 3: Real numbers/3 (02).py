n, i, a = int(input()), 1, 0
while i <= n:
    a += 1 / (i ** 2)
    i += 1
print(a)
