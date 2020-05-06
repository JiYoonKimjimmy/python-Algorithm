year = int(input())

check1 = year % 4 == 0
check2 = year % 100 != 0
check3 = year % 400 == 0

if (check1 & check2) | (check1 & check3):
    print('1')
else:
    print('0')