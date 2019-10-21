a, m, c = list(map(int, input().split())), [], 0
for i in range(a[1]):
    m.append(int(input()))
m.sort()
while c < a[1] and a[0] - m[c] >= 0:
    a[0] = a[0] - m[c]
    c += 1
print(c)
