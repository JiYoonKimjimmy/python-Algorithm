t = int(input())
answers = []
for _ in range(t):
    answers.append(input())
t_s = 0
for i in range(len(answers)):
    answer = answers[i]
    score = 0
    for j in range(len(answer)):
        score = score + 1 if answer[j] == 'O' else 0
        t_s += score
    print(t_s)
    t_s = 0
