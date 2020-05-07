import sys

n = int(sys.stdin.readline())

for i in range(n):
    temp = sys.stdin.readline().split(' ')
    n1 = int(temp[0])
    n2 = int(temp[1])
    print('Case #%s: %s + %s = %s' %(i + 1, n1, n2, n1 + n2))
