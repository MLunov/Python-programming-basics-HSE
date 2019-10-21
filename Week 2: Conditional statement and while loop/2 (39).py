m, n = 0, int(input())
while n:
    if n > m:
        m = n
        c = 1
    elif n == m:
        c += 1
    n = int(input())
print(c)
