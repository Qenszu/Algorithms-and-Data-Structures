from zad8testy import runtests

"""
Sortuje tablice T i idac od najwiekszej ilosc zliczam te wartosci odpowiednio 
odejmujac ile jednostek lodow juz sie roztopilo
"""

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

def ice_cream( T ):
    # tu prosze wpisac wlasna implementacje

    n = len(T)
    merge_sort(T)
    T = T[::-1]

    time = 0
    res = 0
    while time < n and T[time] - time > 0:
        res += T[time] - time
        time += 1

    return res


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ice_cream, all_tests = True )
T = [1, 3, 5, 7, 8]
#print(ice_cream(T))