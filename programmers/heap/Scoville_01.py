import heapq


def solution(scoville, K):
    heap = []
    cnt = 0

    for n in scoville:
        heapq.heappush(heap, n)
    print(heap)
    print('----')
    while heap[0] < K:
        print(len(heap))
        if len(heap) == 0:
            return -1
        temp = heapq.heappop(heap) + (heapq.heappop(heap) * 2)
        print(temp)
        heapq.heappush(heap, temp)
        print(heap)
        cnt += 1
    print('----')
    print(heap)

    return cnt


print(solution([1, 2, 3, 9, 10, 12], 7))
