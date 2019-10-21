f = int(input())
l = int(input())
if l % (l + 1 - f) == 0:
    print('YES')
else:
    print('NO')
