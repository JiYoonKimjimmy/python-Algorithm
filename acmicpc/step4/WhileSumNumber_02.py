import sys

while True:
    try:
        n = sys.stdin.readline().split()
        n1 = int(n[0])
        n2 = int(n[1])
        print(n1 + n2)
    except:
        break
