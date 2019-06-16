import random


def selectionSort(arr):
    for i in range(len(arr), 0, -1):
        max = 0

        for j in range(0, i):
            if arr[j] > arr[max]:
                max = j

        arr[max], arr[j] = arr[j], arr[max]

    return arr


arr = random.sample(range(1, 50), 7) # 랜덤 배열 선언
print(arr) # 정렬 전
print(selectionSort(arr)) # 정렬 후
