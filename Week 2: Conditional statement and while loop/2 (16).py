a, b, c = int(input()), int(input()), int(input())
if a == b and a == c:
    print(3)
elif a == b or a == c or b == c:
    print(2)
else:
    print(0)
