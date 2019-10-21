myDict = {}
for i in range(int(input())):
    w, syn = input().split()
    myDict[w], myDict[syn] = syn, w
print(myDict[input()])
