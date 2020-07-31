A, B, V = map(int, input().split())

N, i = 0, 0

while True:
    N = N + A - B
    if N == V:
        break
    i += 1

print(i)
