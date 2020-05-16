t = int(input())
scores = list(map(int, input().split()))
m_s = max(scores)

print(sum(list(map(lambda i: i / m_s * 100, scores))) / t)
