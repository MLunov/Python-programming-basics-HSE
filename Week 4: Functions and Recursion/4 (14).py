def power(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return (a ** 2) ** (n / 2)  # LOL
    else:
        return a * power(a, n - 1)


print(power(float(input()), float(input())))
