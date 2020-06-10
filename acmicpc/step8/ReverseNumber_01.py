arr = input().split()

m = 0
for s in arr:
    r_s = int(''.join(reversed(s)))
    m = r_s if m < r_s else m

print(m)
