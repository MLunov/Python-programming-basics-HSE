m1, m2, n = 0, 0, int(input())
while n:
    if n >= m1:
        m2 = m1
        m1 = n
    elif n <= m1 and n >= m2 and m2 <= m1:
        m2 = n
    n = int(input())
print(m2)
