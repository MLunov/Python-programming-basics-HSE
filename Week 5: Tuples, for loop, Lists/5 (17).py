s = list(map(int, input().split()))
for i in range(1, len(s)):
    if s[i] > s[i - 1]:
        print(s[i], end=' ')
