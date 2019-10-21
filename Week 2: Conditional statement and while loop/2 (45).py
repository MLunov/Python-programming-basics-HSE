nr, c, m, n = 0, 1, 1, int(input())
while n:
    if n == nr:
        c += 1
        if c > m:
            m = c
    else:
        c = 1
    nr = n
    n = int(input())
print(m)
