s = input().lower()

arr = [0] * 26

for c in s:
    arr[ord(c) - 97] += 1

m = max(arr)
m_c = arr.count(m)
if m_c > 1:
    print('?')
else:
    print(chr(arr.index(m) + 97).upper())
