from kol1testy import runtests

def partition(A, p, r):
    pivot = A[r]
    i = p - 1

    for j in range(p, r):
        if A[j] <= pivot:
            i += 1
            A[j], A[i] = A[i], A[j]

    A[i+1], A[r] = A[r], A[i+1]
    return i + 1

def quickselect(A, p, r, k):
    if p == r:
        return A[p]
    
    q = partition(A, p, r)

    if k == q:
        return A[q]
    elif k < q:
        return quickselect(A, p, q - 1, k)
    else:
        return quickselect(A, q + 1, r, k)

def ksum(T, k, p):
    result = 0
    n = len(T)

    for i in range(n - p + 1):
        tmp = T[i:p+i]
        result += quickselect(tmp, 0, p-1, p-k)

    return result

    

# zmien all_tests na True zeby uruchomic wszystkie testy
#błędy w implementacji
runtests( ksum, all_tests=True )