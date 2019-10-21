def IsPrime(n):
    d = 2
    while d <= n ** (1 / 2):
        if n % d == 0:
            return print('NO')
        d += 1
    return print('YES')


IsPrime(int(input()))
