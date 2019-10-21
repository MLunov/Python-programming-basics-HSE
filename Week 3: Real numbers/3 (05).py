import math

n = float(input())
if n - math.floor(n) >= 0.5:
    print(math.ceil(n))
else:
    print(math.floor(n))
