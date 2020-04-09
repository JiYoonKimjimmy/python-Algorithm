from collections import Counter
from functools import reduce


def solution(clothes):
    # [프로그래머스 문제 : 위장]
    # - array 에 담긴 item 별로 같은 kind 의 요소의 수를 종합
    # - combination(조합) 경우의 수를 이용하여 총 경우의 수를 계산
    # - 각 kind 별로 포함되지 않을 수 있는 경우, +1
    # - 하지만, 모두 포함되지 않는 경우의 수는 없는 조건이므로, -1
    cnt = Counter([kind for name, kind in clothes])
    print('cnt :', cnt)

    answer = reduce(lambda a, b: a * (b + 1), cnt.values(), 1) - 1
    return answer


clothes = [['clothe1', 'a'], ['clothe2', 'a'], ['clothe3', 'b']]
print('Camouflage answer :', solution(clothes))