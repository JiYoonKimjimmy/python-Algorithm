arr = []
for _ in range(10):
    arr.append(int(input()))

print(len(set(list(map(lambda i: i % 42, arr)))))
