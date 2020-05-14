menu = [0] * 5

for i in range(5):
    menu[i] = int(input())

burger = menu[0:3]
drink = menu[3:5]

cp = 0
for b in burger:
    for d in drink:
        temp = b + d - 50
        cp = temp if temp < cp or cp == 0 else cp

print(cp)
