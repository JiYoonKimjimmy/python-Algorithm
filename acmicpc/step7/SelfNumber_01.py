# [셀프 넘버 문제]
# 1부터 10,000까지의 자연수 중 생성자를 가진 숫자가 아닌 숫자를 구하는 문제
# * 숫자의 생성자란?
#     ex. 87의 생성자는? 75 ==> 75 + 7 + 5 = 87 이기 때문에..
# - 풀이 방법
#     1. 1 ~ 10,000까지 자연수 natural numbers 배열을 만든다.
#     2. natural numbers 배열을 loop 하면서 각 숫자별로 생성자를 가진 숫자를 만들어서 새로운 배열에 추가한다.
#     3. 자연수 배열에서 생성자를 가진 수들의 배열을 빼면, 셀프 넘버 숫자 배열만 남는다.
n_numbers = set(range(1, 10001))
g_numbers = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    g_numbers.add(i)

s_numbers = n_numbers - g_numbers
for n in sorted(s_numbers):
    print(n)