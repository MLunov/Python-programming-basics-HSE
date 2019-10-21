n, s, x, min = int(input()), list(map(int, input().split())), \
               int(input()), float('inf')
for i in range(n):
    if abs(s[i] - x) < min:
        min = abs(s[i] - x)
        near_x = s[i]
print(near_x)
