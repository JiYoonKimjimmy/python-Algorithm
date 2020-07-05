s = input()

r_arr = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for r in r_arr:
    s = s.replace(r, '*')

print(len(s))
