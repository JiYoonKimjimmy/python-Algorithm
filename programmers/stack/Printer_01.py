from collections import deque


def solution(properties, location):
    arr = []
    dq = deque()
    for i, e in enumerate(properties):
        dq.append((i, e))

    while dq:
        cur_p = dq.popleft()
        if dq and cur_p[1] < max(dq, key=lambda q: q[1])[1]:
            dq.append(cur_p)
        else:
            arr.append(cur_p[0])

    return arr.index(location) + 1


print(solution([1, 1, 9, 1, 1, 1], 0))
