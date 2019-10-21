s, max = list(map(int, input().split())), 0
for i in range(len(s)):
    if s[i] >= max:
        max = s[i]
        ind = i
print(max, ind)
