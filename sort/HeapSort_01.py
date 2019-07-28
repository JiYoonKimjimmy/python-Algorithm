import random


def heap_sort(arr):
    size = len(arr)

    # 먼저, 배열을 heap 구조로 설정
    for i in range(size, 0, -1):
        heapify(arr, size, i)

    # heap sort
    for i in range(size, 1, -1):
        arr[0], arr[i - 1] = arr[i - 1], arr[0]
        heapify(arr, i - 1, 1)

    return arr


def heapify(arr, size, root):
    child = root * 2    # root 로부터 왼쪽 child

    while child <= size:
        # child index 가 배열 크기를 초과 안하는 경우
        if child < size and arr[child - 1] < arr[child]:
            # child < size 는 오른쪽 child 가 없는 경우는 마지막 node 인 경우 밖에 없음.
            # 왼쪽 child 와 오른쪽 child 를 비교하여,
            # 왼쪽 child 가 더 작다면, 큰 값이 child 가 되도록 설정
            child += 1

        if arr[root - 1] < arr[child - 1]:
            # root 가 child 보다 더 작다면 swap
            arr[root - 1], arr[child - 1] = arr[child - 1], arr[root - 1]

        root = child
        child = root * 2


arr = random.sample(range(1, 50), 7)
print(arr)
print(heap_sort(arr))