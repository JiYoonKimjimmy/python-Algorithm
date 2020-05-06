alarm = input()
a = alarm.split(' ')
h = int(a[0])
m = int(a[1])

if (h == 0) & (m < 45):
    h = 24

total = (h * 60) + m - 45
hh = total // 60
mm = total - (hh * 60)

print(hh, mm)
