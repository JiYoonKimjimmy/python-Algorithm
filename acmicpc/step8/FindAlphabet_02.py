s = input()

print(*map(s.find, map(chr, range(97, 123))), sep=" ")
