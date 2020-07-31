A, B, V = map(int, input().split())

answer = (V - B) / (A - B)

print(int(answer) + 1 if answer % 1 > 0 else int(answer))