s = input()

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
answer = 0
for c in s:
    answer += dial.index(list(filter(lambda d_s: d_s.count(c) > 0, dial))[0]) + 2

answer += len(s)

print(answer)
