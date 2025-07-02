from kol1btesty import runtests

def merge_sort(arr):
    size = len(arr)
    # Base case: if the array has one or no elements, it is already sorted
    if size > 1:
        # Split the array into two halves
        left_arr = arr[:size//2]
        right_arr = arr[size//2:]

        # Recursively sort each half
        merge_sort(left_arr)
        merge_sort(right_arr)

        # Initialize pointers for left_arr, right_arr, and the main array
        i = 0 
        j = 0
        k = 0

        # Merge the sorted halves back into the main array
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        # Copy any remaining elements of left_arr, if any
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1                                                        
            k += 1                                                           

        # Copy any remaining elements of right_arr, if any
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

def turn_into_arr(str):
    n = len(str)
    arr = []
    for i in range(n):
        arr.append(str[i])

    merge_sort(arr)
    return arr

def sort_str_arr(T, n):
    for i in range(n):
        T[i] = turn_into_arr(T[i])
    
    merge_sort(T)

def f(T):
    n = len(T)
    sort_str_arr(T, n)
    maxi = 0
    cnt = 1
    for i in range(n-1):
        if T[i] == T[i+1]:
            cnt += 1
        else:
            maxi = max(maxi, cnt)
            cnt = 1  # Reset count to 1 instead of 0

    maxi = max(maxi, cnt)  # Check the last sequence
    return maxi 

# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( f, all_tests=True )
