a = int(input())
sim1 = (a // 10**3) % 10 - (a % 10)
sim2 = (a // 10**2) % 10 - (a // 10) % 10
print(1 + sim1**2 + sim2**2)
