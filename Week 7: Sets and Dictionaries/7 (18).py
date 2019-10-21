import sys

myDict, myList = {}, []
for line in sys.stdin:
    for w in line.split():
        myDict[w] = myDict.get(w, 0) + 1
for w in myDict:
    myList.append((myDict[w], w))
myList.sort(key=lambda x: (-x[0], x[1]))
for i in range(len(myList)):
    print(myList[i][1])
