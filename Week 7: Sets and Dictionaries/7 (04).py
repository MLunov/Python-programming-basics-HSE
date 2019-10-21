myList = input().split()
mySet = set()
for i in myList:
    if i not in mySet:
        mySet.add(i)
        print('NO')
    else:
        print('YES')
