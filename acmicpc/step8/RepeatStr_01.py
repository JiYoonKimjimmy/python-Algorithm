n = int(input())

for _ in range(n):
    r, s = input().split()
    t = ''
    for i in s:
        t += i * int(r)

    print(t)
