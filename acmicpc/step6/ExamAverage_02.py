case = int(input())

l_case = []
for _ in range(case):
    l_case.append(list(map(int, input().split())))

for d_case in l_case:
    # 전체 학생수
    s_c = d_case[0]
    # 전체 점수 목록
    scores = d_case[1:]
    # 전체 평균
    average = sum(scores) / s_c
    # 평균을 넘는 학생수
    ps_c = len(list(filter(lambda i: i > average, scores)))
    print('%.3f' % (ps_c / s_c * 100), end='')
    print('%')
