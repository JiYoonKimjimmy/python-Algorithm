import sys

n = sys.stdin.readline().strip()
if len(n) < 2:
    n = '0' + n
t = ''
cnt = 0
while n != t:
    if t == '':
        t = n
    n1, n2 = t[0], t[1]
    s = str(int(n1) + int(n2))
    if len(s) < 2:
        s = '0' + s
    t = n2 + s[1]
    cnt += 1

print(cnt)
