total = 0

for i in range(5):
    score = int(input())
    total += score if score >= 40 else 40

print('%i' %(total / 5))