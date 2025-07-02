def counting_sort(A):
    # Get the length of the array
    n = len(A)
    # Find the maximum and minimum values in the array
    maxi = max(A)
    mini = min(A)
    # Create a count array with a size based on the range of input values
    count_arr = [0] * (maxi - mini + 1)

    # Count the occurrences of each value in the input array
    for i in range(n):
        count_arr[A[i] - mini] += 1

    # Update the count array to store the cumulative count of elements
    for i in range(1, maxi - mini + 1):
        count_arr[i] += count_arr[i - 1]
    
    # Create a result array to store the sorted output
    result_arr = [0] * n

    # Build the sorted array by placing elements at their correct positions
    for i in range(n - 1, -1, -1):
        result_arr[count_arr[A[i] - mini]-1] = A[i]
        count_arr[A[i] - mini] -= 1

    return result_arr

# Example usage
A = [2, 1, 4, 2, 4, 2]
A = counting_sort(A)
print(A)
