n = int(input())
m, stage = 1, 1

while m + stage <= n:
    m += stage
    stage += 1

step = n - m;

x, y = step + 1, stage - step

if stage % 2 == 0:
    print('{}/{}'.format(x, y))
else:
    print('{}/{}'.format(y, x))
