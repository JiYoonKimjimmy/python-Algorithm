from collections import Counter
from functools import reduce


def solution(clothes):
    cnt = Counter([kind for name, kind in clothes])
    print('cnt :', cnt)

    answer = reduce(lambda a, b: a * (b + 1), cnt.values(), 1) - 1
    return answer


clothes = [['clothe1', 'a'], ['clothe2', 'a'], ['clothe3', 'b']]
print('Camouflage answer :', solution(clothes))