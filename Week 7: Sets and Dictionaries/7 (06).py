import sys

text = sys.stdin
mySet = set()
for line in text:
    for w in line.split():
        mySet.add(w)
print(len(mySet))
