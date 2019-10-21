# inFile = open('input.txt', 'r', encoding='utf8') # - для coursera с указанием юникода
inFile = open('input.txt', 'r')
outFile = open('output.txt', 'w', encoding='utf8')
l = [list(line.strip().split()) for line in inFile]
l.sort()
for line in l:
    line.pop(2)
    print(*line, end='\n', file=outFile)
inFile.close()
outFile.close()
