def gcd(a, b):
    if b != 0:
        return gcd(b, a % b)
    return a


def ReduceFraction(n, m):
    nod = gcd(n, m)
    if gcd(n, m) != 1:
        return ReduceFraction(n / nod, m / nod)
    else:
        return int(n), int(m)


print(*ReduceFraction(int(input()), int(input())))
