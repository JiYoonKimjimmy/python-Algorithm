n = int(input())

star = []

for i in range(n, 0, -1):
    star.append(' ' * (n - i) + '*' * (2 * i - 1))
for s in star:
    print(s)

star.reverse()
for i in range(len(star)):
    if i != 0:
        print(star[i])
