# [한수 문제]
# 1 ~ N(입력수)까지 한수가 몇 개있는지 구하는 문제
# * 한수 : 각 자릿수가 등차수열을 이루고 있는 숫자
# * 등차수열 : 차이가 일정한 수열
# (N은 1,000보다 작은 수)

n = int(input())
hansu = 0

for i in range(1, n + 1):
    if i <= 99:
        hansu += 1
    else:
        nums = list(map(int, str(i)))
        if nums[0] - nums[1] == nums[1] - nums[2]:
            hansu += 1

print(hansu)
