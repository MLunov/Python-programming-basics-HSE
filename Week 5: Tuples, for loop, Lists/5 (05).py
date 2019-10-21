amount = int(input())
print(amount * "+___ ")
for i in range(1, amount + 1):
    print("|" + str(i) + " / ", end='')
print('\n' + amount * "|__\ ")
print(amount * "|    ")
