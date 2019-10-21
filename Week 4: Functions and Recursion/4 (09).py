def MinDivisor(n):
    d = 2
    while d <= n ** (1 / 2):
        if n % d == 0:
            return d
        d += 1
    return n


print(MinDivisor(int(input())))
