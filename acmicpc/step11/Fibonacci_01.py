num = int(input())

arr = [0] * (num + 1)
for i in range(len(arr)):
    if arr[i - 1] == 0:
        arr[i] = arr[i - 1] + i
    else:
        arr[i] = arr[i - 2] + arr[i - 1]

print(arr[num])
