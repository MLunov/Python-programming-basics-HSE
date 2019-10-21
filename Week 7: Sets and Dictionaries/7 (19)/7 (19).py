# inFile = open('input.txt', 'r', encoding='utf8') # - для coursera с указанием юникода
inFile = open('input.txt', 'r')
outFile = open('output.txt', 'w', encoding='utf8')
myDict, myList, c = {}, [], 0
for w in inFile:
    myDict[w.strip()] = myDict.get(w.strip(), 0) + 1
myDict.pop('', None)
for w in myDict:
    myList.append((myDict[w], w))
    c += myDict[w]
myList.sort(key=lambda x: (-x[0], x[1]))
if myList[0][0] / c * 100 > 50:
    print(myList[0][1], file=outFile)
else:
    print(myList[0][1], file=outFile)
    print(myList[1][1], file=outFile)

inFile.close()
outFile.close()
