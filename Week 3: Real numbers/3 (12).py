a, b, c = float(input()), float(input()), float(input())
d, e, f = float(input()), float(input()), float(input())
if (a and d) != 0 or (b and c) != 0:
    x = (e * d - b * f) / (a * d - b * c)
    if b != 0:
        print(x, (e - a * x) / b)
    elif d != 0:
        print(x, (f - c * x) / d)
    else:
        print(x, 0)
