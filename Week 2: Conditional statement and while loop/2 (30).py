x = float(input())
y = float(input())
i = 1
while x < y:
    x += 0.1 * x
    i += 1
print(i)
