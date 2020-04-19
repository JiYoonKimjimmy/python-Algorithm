def solution(heights):
    # [프로그래머스 문제 : 탑]
    # - array 의 이전 element 들 중에 큰 값이 있다면,
    # - 해당 index 를 return
    answer = [0] * len(heights)

    for i in range(len(heights) - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            if heights[i] < heights[j]:
                answer[i] = j + 1
                break

    return answer


heights = [3, 9, 9, 3, 5, 7, 2]
print(solution(heights))