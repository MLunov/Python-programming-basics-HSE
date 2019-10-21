n = int(input())
print(n, 'korov', end='')
if n % 10 == 0 or 4 < n % 10 < 10 or 10 < n % 100 < 15:
    print('')
elif 1 < n % 10 < 5:
    print('y')
else:
    print('a')
