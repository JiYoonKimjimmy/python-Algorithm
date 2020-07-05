def checker(word):
    stack = []
    for i in range(len(word)):
        c = word[i]

        if c not in stack:
            stack.append(c)
        else:
            if (i != 0) & (word[i] != word[i - 1]):
                return 0

    return 1


n = int(input())

words = []

for _ in range(n):
    words.append(input())

answer = 0
for word in words:
    answer += checker(word)

print(answer)
