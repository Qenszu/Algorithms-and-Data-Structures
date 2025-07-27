def insertion_sort(A):
    # Traverse through 1 to len(A)
    for i in range(1, len(A)): 
        key = A[i]  # Element to be placed at the correct position
        j = i - 1
        
        # Move elements of A[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < A[j]:
            A[j+1] = A[j]
            j -= 1

        A[j+1] = key  # Place key at after the element just smaller than it

# Example usage
A = [5, 3, 8, 6, 2]
insertion_sort(A)
print("Posortowana tablica:", A)  # Output the sorted array