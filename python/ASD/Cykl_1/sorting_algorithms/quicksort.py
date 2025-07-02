def quicksort(A, p, r):
    # If the array has more than one element
    if p < r:
        # Partition the array and get the pivot index
        q = partition(A, p, r)
        # Recursively sort the elements before and after partition
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)

def partition(A, p, r):
    # Choose the last element as the pivot
    pivot = A[r]
    # Index of the smaller element
    i = p-1

    # Traverse through all elements
    for j in range(p, r):
        # If the current element is smaller than or equal to the pivot
        if A[j] <= pivot:
            # Increment the index of the smaller element
            i += 1
            # Swap the elements
            A[i], A[j] = A[j], A[i]
    
    # Swap the pivot element with the element at i+1
    A[i+1], A[r] = A[r], A[i+1]
    # Return the partition index
    return i + 1

# Example usage
A = [1, 5, 2, 3, 2, 8, 6, 8, 9, 3]
# Sort the array
quicksort(A, 0, len(A)-1)
# Print the sorted array
print(A)
