s = input()
inp = s.find('f')
if inp != -1:
    outp = s[inp + 1:].find('f')
    if outp != -1:
        print(inp + 1 + outp)
    else:
        print(-1)
else:
    print(-2)
