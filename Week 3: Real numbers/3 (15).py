s = input()
inp = s.find('f')
if inp != -1:
    print(inp)
    out = s[-1::-1].find('f')
    if (len(s) - 1 - out) != inp:
        print(len(s) - 1 - out)
