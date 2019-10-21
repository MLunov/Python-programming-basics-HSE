s, min = list(map(int, input().split())), float('inf')
for i in range(len(s)):
    if s[i] > 0 and s[i] < min:
        min = s[i]
print(min)
