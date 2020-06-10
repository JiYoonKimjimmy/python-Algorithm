s = input()

arr = [-1] * 26
for i in range(len(s)):
    c = s[i]
    if arr[ord(c) - 97] == -1:
        arr[ord(c) - 97] = i

for o in arr:
    print(o, end=' ')
