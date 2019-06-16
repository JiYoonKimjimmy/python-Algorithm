import random


def bubbleSort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


arr = random.sample(range(1, 50), 7)
print(arr)
print(bubbleSort(arr))
