import math

price = float(input())
print(math.floor(price), round(100 * (price - math.floor(price))))
