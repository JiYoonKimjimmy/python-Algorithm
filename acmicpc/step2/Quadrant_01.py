x = int(input())
y = int(input())

check1 = x >= 0
check2 = y >= 0

if check1 & check2:
    print('1')
elif (not check1) & check2:
    print('2')
elif (not check1) & (not check2):
    print('3')
else:
    print('4')