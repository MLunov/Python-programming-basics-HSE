# говнокод
mut_set, all_set = set(), set()
N = int(input())
for j in range(int(input())):
    mut_set.add(input())
all_set |= mut_set
for i in range(1, N):
    st_set = set()
    for j in range(int(input())):
        st_set.add(input())
    mut_set &= st_set
    all_set |= st_set
print(len(mut_set))
for i in mut_set:
    print(i)
print(len(all_set))
for i in all_set:
    print(i)
