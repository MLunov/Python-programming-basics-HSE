s = list(map(int, input().split()))
for i in range(1, len(s), 2):
    s[i - 1], s[i] = s[i], s[i - 1]
print(*s)
