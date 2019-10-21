def CountSort(A):
    sort_A = [0] * (max(A) + 1)
    for i in A:
        sort_A[i] += 1
    for i in range(len(sort_A)):
        print((str(i) + ' ') * sort_A[i], end='')


CountSort(list(map(int, input().split())))
