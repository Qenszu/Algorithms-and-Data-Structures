def heapify_rek(arr, size, i):
    # Initialize largest as root
    largest = i
    left = 2*i + 1
    right = 2*i + 2

    # Check if left child exists and is greater than root
    if left < size and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than largest so far
    if right < size and arr[right] > arr[largest]:
        largest = right 

    # Change root if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # Recursively heapify the affected sub-tree
        heapify_rek(arr, size, largest)

def heapify_ite(arr, size, i):
    while True:
        # Initialize largest as root
        largest = i  
        left = 2 * i + 1  
        right = 2 * i + 2  

        # Check if left child exists and is greater than root
        if left < size and arr[left] > arr[largest]:
            largest = left

        # Check if right child exists and is greater than largest so far
        if right < size and arr[right] > arr[largest]:
            largest = right

        # Change root if needed
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            i = largest  
        else:
            break  

def heapsort(arr):
    size = len(arr)

    # Build a maxheap
    for i in range(size // 2 - 1, -1, -1):
        heapify_rek(arr, size, i)

    # One by one extract elements
    for i in range(size - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] 
        heapify_rek(arr, i, 0)

# Example usage
arr = ["pies", "mysz", "kot", "kogut", "tok", "seip", "kot"]
heapsort(arr)
print("Posortowana tablica:", arr)