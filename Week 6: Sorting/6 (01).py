def merge(A, B):
    len_A, len_B = len(A), len(B)
    C = []
    i, j = 0, 0
    while i < len_A and j < len_B:
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
    if i < len_A:
        C.extend(A[i:])
    else:
        C.extend(B[j:])
    return (print(*C))


A = list(map(int, input().split()))
B = list(map(int, input().split()))
merge(A, B)
