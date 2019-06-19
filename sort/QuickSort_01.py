import random


def quickSort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left, right, equal = [], [], []

    for i in arr:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        else:
            equal.append(i)

    return quickSort(left) + equal + quickSort(right)


arr = random.sample(range(1, 50), 7)
print(arr)
print(quickSort(arr))