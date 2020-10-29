def solution(a, b):
    answer = []

    for _ in range(len(a)):
        total = 0
        for i in list(map(lambda k: k[0] * k[1], zip(a, b))):
            total += i
        answer.append(total)

        # b array 왼쪽으로 shift
        b.append(b.pop(0))

    return min(answer)


print(solution([1, 4, 2], [4, 5, 3]))
print(solution([1], [2]))
