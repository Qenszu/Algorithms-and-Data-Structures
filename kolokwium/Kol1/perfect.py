from kol1testy import runtests

def insertion_sort(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1
        
        A[j+1] = key

def bucket_sort(A, mini, maxi):
    n = len(A)
    bucket_range = (maxi - mini)/n
    buckets = [[] for _ in range(n)]

    for num in A:
        ind = int((num - mini)/bucket_range)
        if ind == n:
            ind -= 1

        buckets[ind].append(num)
    
    result = [] * n

    for bucket in buckets:
        insertion_sort(bucket)
        result.extend(bucket)

    return result

def partition(A, p, r):  
    x = A[r]
    i = p - 1

    for j in range(p, r):
        if A[j] < x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i + 1

def quickselect(A, p, r, k):
    if p == r:
        return A[r]  
    q = partition(A, p, r)  

    if q == k:
        return A[k]
    elif q < k:  
        return quickselect(A, q + 1, r, k)
    else:  
        return quickselect(A, p, q - 1, k)

def ogrodzenie(M, D, T):
    n = len(T)
    left = []
    right = []
    p = quickselect(T, 0, n-1, n//2)


    for i in range(n):
        if T[i] < p:
            left.append(T[i])
        else:
            right.append(T[i])

    left = bucket_sort(left, 0, p)
    right = bucket_sort(right, p, M)

    left.extend(right)
    cnt = 0
    for i in range(n-1):
        if left[i+1]-left[i] > D:
            cnt += 1

    return cnt

runtests( ogrodzenie, all_tests = True )