def quickselect(A, p, r, k):
    # If the list contains only one element, return that element
    if p == r:
        return A[p]
    
    # Partition the array and get the pivot index
    q = partition(A, p, r)
    
    # If the pivot index is the k-th element, return it
    if k == q:
        return A[q]
    # If k is less than the pivot index, recursively call quickselect on the left subarray
    elif k < q:
        return quickselect(A, p, q - 1, k)
    # If k is greater than the pivot index, recursively call quickselect on the right subarray
    else:
        return quickselect(A, q + 1, r, k)
        

def partition(A, p, r):
    # Choose the last element as the pivot
    pivot = A[r]
    i = p - 1
    
    # Rearrange the elements based on the pivot
    for j in range(p, r):
        if A[j] < pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    
    # Place the pivot in its correct position
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

# Example usage
A = [1, 3, 5, 7, 8]
A = [1, 3, 3, 2, 2]
n = len(A)
k = n - 1
print(k, "-ty elemento to: ", quickselect(A, 0, n - 1, n-k))