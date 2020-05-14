arr = input().split()

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if int(arr[i]) > int(arr[j]):
            arr[i], arr[j] = arr[j], arr[i]

print(arr[1])
