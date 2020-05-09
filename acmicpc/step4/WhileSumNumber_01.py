import sys

n1, n2 = 1, 1
while n1 > 0 and n2 > 0:
    n = sys.stdin.readline().split(' ')
    n1 = int(n[0])
    n2 = int(n[1])
    if n1 != 0 and n2 != 0:
        print(n1 + n2)