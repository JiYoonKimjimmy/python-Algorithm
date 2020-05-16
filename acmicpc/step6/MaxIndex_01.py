arr = []
for _ in range(9):
    arr.append(int(input()))

m_n = max(arr)
print(m_n)
print(arr.index(m_n) + 1)
