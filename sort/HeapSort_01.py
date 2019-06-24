import random


def heap_sort(arr):
    size = len(arr)

    for i in range(size, 0, -1):
        heapify(arr, size, i)

    for i in range(size, 1, -1):
        arr[0], arr[i - 1] = arr[i - 1], arr[0]
        heapify(arr, i - 1, 1)

    return arr


def heapify(arr, size, root):
    child = root * 2

    while child <= size:
        if child < size and arr[child - 1] < arr[child]:
            child += 1

        if arr[root - 1] < arr[child - 1]:
            arr[root - 1], arr[child - 1] = arr[child - 1], arr[root - 1]

        root = child
        child = root * 2


arr = random.sample(range(1, 50), 7)
print(arr)
print(heap_sort(arr))