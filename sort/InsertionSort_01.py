import random


def insertionSort(arr):
    for i in range(1, len(arr)):
        while 0 < i and arr[i] < arr[i - 1]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1
    return arr


arr = random.sample(range(1, 50), 7)
print(arr)
print(insertionSort(arr))