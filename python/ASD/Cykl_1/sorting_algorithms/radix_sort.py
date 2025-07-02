from math import log10

def counting_sort(tmp, A):
    # Initialize variables
    n = len(A)
    maxi = max(tmp)
    mini = min(tmp)
    count_arr = [0] * (maxi - mini + 1)

    # Count occurrences of each digit
    for i in range(n):
        count_arr[tmp[i] - mini] += 1

    # Accumulate counts
    for i in range(1, maxi - mini + 1):
        count_arr[i] += count_arr[i - 1]
    
    # Build the sorted array
    result_arr = [0] * n
    for i in range(n - 1, -1, -1):
        result_arr[count_arr[tmp[i] - mini]-1] = A[i]
        count_arr[tmp[i] - mini] -= 1

    return result_arr

def key_arr(A, k): # k --> key digit
    # Extract the k-th digit from each number
    n = len(A)
    res = [0] * n

    for i in range(n):
        key = (A[i]//10**(k))%10
        res[i] = key
    
    return res

def radix_sort(A):
    # Determine the number of digits in the largest number
    k = int(log10(max(A))) + 1

    # Perform counting sort for each digit
    for i in range(k):
        tmp = key_arr(A, i)
        A = counting_sort(tmp, A)

    return A

# Example usage
A = [126,3656,334,347,3765,253,213,63,75,48,8,6]
A = radix_sort(A)
print(A)
