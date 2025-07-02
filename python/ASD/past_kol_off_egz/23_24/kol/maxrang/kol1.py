from kol1testy import runtests

"""
Algorytm wykorzystuje mechanizm sortowania mergesort ktory przy kazdym
porownywaniu lewej tablicy z prawa zlicza liczbe inwersji 
"""

def merge_sort(arr, ans):
    size = len(arr)
    if size > 1:
        left = arr[:size//2]
        right = arr[size//2:]

        merge_sort(left, ans)
        merge_sort(right, ans)

        i = 0 
        j = 0
        k = 0 

        while i < len(left) and j < len(right):
            if left[i][0] < right[j][0]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                ans[right[j][1]] += i
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            ans[right[j][1]] += i
            arr[k] = right[j]
            j += 1
            k += 1

    return arr

def maxrank(arr):
    ans = [0 for _ in range(len(arr))]
    tmp = [0 for _ in range(len(arr))]
    for i in range(len(arr)):
        tmp[i] = (arr[i], i)

    merge_sort(tmp, ans)
    return max(ans)
  

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maxrank, all_tests = True )
