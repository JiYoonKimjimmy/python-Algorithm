def solution(a, b):
    answer = 0
    BEST = -1
    WORST = 0

    a.sort()
    b.sort()

    def get_least_rating(start, end):
        # a의 가장 쎈 상대를 이길 수 있는 선수 중에 가장 약한 선수 찾기
        # 이진 탐색 기법
        while start < end:
            mid = (start + end) // 2
            if b[mid] > a[BEST]:
                end = mid
            else:
                start = mid + 1
        return end

    while a:
        if a[BEST] >= b[BEST]:
            # a의 가장 쎈 선수의 상대에겐 무조건 b의 제일 약한 선수 매칭
            b.pop(WORST)
        else:
            # 현재 가장 약한 선수 찾기
            b_least_rating = get_least_rating(0, len(b) - 1)
            b.pop(b_least_rating)
            answer += 1
        a.pop(BEST)

    return answer


print(solution([17, 8, 2, 16], [4, 4, 12, 16]))
