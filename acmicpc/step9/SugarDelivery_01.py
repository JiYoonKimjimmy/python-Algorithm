def sol(n):
    # [백준 2839. 설탕 배달]
    # - (3 * x) + (5 * y) 의 최솟값을 찾는 문제
    # - 3의 약수 중에 최솟값을 먼저 찾아 5의 약수를 더하는 방식
    for x in range((n // 3) + 1):
        for y in range((n // 5) + 1):
            print(x, '-', y)
            if (x * 3 + y * 5) == n:
                return x + y

    return -1


n = int(input())

print(sol(n))
