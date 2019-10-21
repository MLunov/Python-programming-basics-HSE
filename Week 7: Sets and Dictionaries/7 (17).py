import sys

myDict, myVal = {}, {}
for line in sys.stdin:
    for w in line.split():
        myDict[w] = myDict.get(w, 0) + 1
for w in myDict:
    if myDict[w] not in myVal:
        myVal[myDict[w]] = []
    myVal[myDict[w]].append(w)
print(sorted(myVal[max(myVal)])[0])
