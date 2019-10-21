def sum(n):
    if n == 0:
        return 0
    if n != 0:
        return n + sum(int(input()))


print(sum(int(input())))
