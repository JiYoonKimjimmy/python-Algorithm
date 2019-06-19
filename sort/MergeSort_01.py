import random

def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    left = mergeSort(arr[:len(arr) // 2])
    right = mergeSort(arr[len(arr) // 2:])

    i, j, k = 0, 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    if i == len(left):
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    else:
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

    return arr


arr = random.sample(range(1, 50), 7)
print(arr)
print(mergeSort(arr))

