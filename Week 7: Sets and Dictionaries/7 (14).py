myDict = {}
for line in open('input.txt'):
    for w in line.split():
        myDict[w] = myDict.get(w, -1) + 1
        print(myDict[w], end=' ')
