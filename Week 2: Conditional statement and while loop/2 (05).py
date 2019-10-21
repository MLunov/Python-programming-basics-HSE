xb = int(input())
yb = int(input())
xf = int(input())
yf = int(input())
if xf == xb - 1 and (yf == yb - 1 or yf == yb or yf == yb + 1):
    print('YES')
elif xf == xb + 1 and (yf == yb - 1 or yf == yb or yf == yb + 1):
    print('YES')
elif xf == xb and (yf == yb - 1 or yf == yb + 1):
    print('YES')
else:
    print('NO')
