s = list(map(int, input().split()))
n_s = s.copy()
n_s[s.index(max(s))], n_s[s.index(min(s))] = s[s.index(min(s))], \
                                             s[s.index(max(s))]
print(*n_s)
