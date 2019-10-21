a, b, c = float(input()), float(input()), float(input())
x1 = (- b + (b ** 2 - 4 * a * c) ** (1 / 2)) / (2 * a)
x2 = (- b - (b ** 2 - 4 * a * c) ** (1 / 2)) / (2 * a)
if b ** 2 - 4 * a * c < 0:
    print()
elif abs(x1 - x2) < 10 ** (-6):
    print(x1)
elif x1 < x2:
    print(x1, x2)
else:
    print(x2, x1)
