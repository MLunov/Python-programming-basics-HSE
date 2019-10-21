s = input()
inp = s.find('h')
outp = len(s) - s[-1::-1].find('h')
print(s[:inp] + s[outp:])
