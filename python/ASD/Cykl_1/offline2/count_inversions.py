""""Patryk Opala
    Funkcja wykorzystuje algorytm sortowania merge sort. Dodatkowo w momencie
    gdy w prawej części podzielonej tablicy wystepuje element mniejszy od
    elementu w lewej części zmienna cnt zwiększana jest o ilość elementów
    które pozostały w lewej części tablicy"""

from zad2testy import runtests

def count_inversions(A):
    cnt = 0  # Initialize the inversion count to zero

    def merge_sort(arr):
        nonlocal cnt  # Use the outer scope variable cnt
        size = len(arr)
        if size > 1:
            # Split the array into two halves
            left_arr = arr[:size//2]
            right_arr = arr[size//2:]

            # Recursively sort both halves
            merge_sort(left_arr)
            merge_sort(right_arr)

            # Merge the sorted halves and count inversions
            i = 0 
            j = 0
            k = 0
            while i < len(left_arr) and j < len(right_arr):
                if left_arr[i] < right_arr[j]:
                    arr[k] = left_arr[i]
                    i += 1
                else:
                    cnt += len(left_arr) - i  # Count inversions
                    arr[k] = right_arr[j]
                    j += 1
                k += 1

            # Copy any remaining elements of left_arr
            while i < len(left_arr):
                arr[k] = left_arr[i]
                i += 1                                                        
                k += 1                                                           

            # Copy any remaining elements of right_arr
            while j < len(right_arr):
                arr[k] = right_arr[j]
                j += 1
                k += 1

    merge_sort(A)  # Call the merge_sort function
    return cnt  # Return the total count of inversions


# Odkomentuj by uruchomic duze testy
# runtests( strong_string, all_tests=True )

# Zakomentuj gdy uruchamiasz duze testy
runtests( count_inversions, all_tests=True )
