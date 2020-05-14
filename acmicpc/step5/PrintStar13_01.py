n = int(input())

mok = n // 2
na = n % 2

for i1 in range(1, n + 1):
    for i2 in range(1, n + 1):
        print('*\t\t', end='')
        if na == 0:
            # n 짝수인 경우
            if i2 == mok:
                print()
                print('\t', end='')
        else:
            # n 홀수인 경우
            if i2 == mok + na:
                print()
                print('\t', end='')
    print()
