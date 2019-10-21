def IsPointCircle(x, y, xc, yc, r):
    return (xc - x) ** 2 + (yc - y) ** 2 <= r ** 2


if IsPointCircle(float(input()), float(input()), float(input()),
                 float(input()), float(input())):
    print('YES')
else:
    print('NO')
