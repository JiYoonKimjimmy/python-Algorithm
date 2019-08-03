import random


def count_sort(arr):
    if (min(arr) < 0):
        # min 값이 0 보다 작다면 예외 발생
        raise

    i, n, k = 0, len(arr), max(arr) + 1
    c = [0] * k

    for j in range(n):
        c[arr[j]] = c[arr[j]] + 1

    for j in range(k):
        while c[j] > 0:
            (arr[i], c[j], i) = (j, c[j] - 1, i + 1)

    return arr


arr = random.sample(range(1, 50), 7)
print(arr)
print(count_sort(arr))