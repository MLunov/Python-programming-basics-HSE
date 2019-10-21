l = []
for i in range(int(input())):
    f, s = input().split()
    l.append((int(s), f))
sort_l = sorted(l, reverse=True)
for i in range(len(l)):
    print(sort_l[i][1])
