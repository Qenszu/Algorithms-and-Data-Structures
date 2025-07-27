def insertion_sort(A):
    # Traverse through 1 to len(A)
    for i in range(1, len(A)): 
        key = A[i]                            
        j = i - 1
        
        # Move elements of A[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < A[j]:
            A[j+1] = A[j]
            j -= 1

        A[j+1] = key

def bucket_sort(A):
    n = len(A)

    # If the array is empty, return it
    if n == 0:
        return A
    
    #creating bucketc
    mini = min(A)
    maxi = max(A)
    bucket_range = (maxi - mini) / n
    buckets = [[] for _ in range(n)]

    #separating elements into buckets 
    for num in A:
        ind = int((num - mini) / bucket_range)
        if ind == n:
            ind -= 1
        
        buckets[ind].append(num)

    #sorting bucketss        
    sorted_A = []

    for bucket in buckets:
        insertion_sort(bucket)
        sorted_A.extend(bucket)

    return sorted_A

# Example usage
A = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
A = bucket_sort(A)
print("Posortowana tablica:", A)