def partition(arr, left, right):
    """Partycjonowanie tablicy wokół pivota (ostatni element)"""
    pivot_value = arr[right]
    store_index = left

    for i in range(left, right):
        if arr[i] < pivot_value:
            arr[i], arr[store_index] = arr[store_index], arr[i]
            store_index += 1

    arr[store_index], arr[right] = arr[right], arr[store_index]  # Przenieś pivot na właściwe miejsce
    return store_index

def quickselect(arr, left, right, k):
    """Znajduje k-ty najmniejszy element w arr[left:right+1]"""
    while left < right:
        pivot_index = partition(arr, left, right)

        if k == pivot_index:
            return arr[k]
        elif k < pivot_index:
            right = pivot_index - 1
        else:
            left = pivot_index + 1
    
    return arr[left]  # Kiedy left == right

def median(T):
    N = len(T)
    elements = [T[i][j] for i in range(N) for j in range(N)]  # Zamiana macierzy na listę
    print(elements)

    median_index = (N * (N - 1)) // 2  # Indeks pierwszego elementu przekątnej
    median_value = quickselect(elements, 0, len(elements) - 1, median_index)

    small_values = [x for x in elements if x < median_value]
    large_values = [x for x in elements if x > median_value]

    small_values.sort()
    large_values.sort(reverse=True)

    # Odbudowa macierzy
    small_index, large_index = 0, 0

    for i in range(N):
        for j in range(N):
            if i == j:
                T[i][j] = median_value
            elif i < j:
                T[i][j] = large_values[large_index]
                large_index += 1
            else:
                T[i][j] = small_values[small_index]
                small_index += 1

# Przykład
T = [
    [2, 7, 5],
    [3, 17, 13],
    [11, 19, 23]
]

median(T)

for row in T:
    print(row)
