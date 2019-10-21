p, x, y = int(input()) / 100, int(input()), int(input())
dep = ((x * 100 + y) + p * (x * 100 + y))
print(int(dep // 100), int(dep % 100))
