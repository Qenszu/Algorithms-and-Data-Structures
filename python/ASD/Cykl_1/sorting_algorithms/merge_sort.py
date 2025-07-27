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

# Test the merge_sort function with a sample array
arr_test = [4, 1, 5, 6, 7, 1, 4, 2, 5, 3]
merge_sort(arr_test)
print(arr_test)