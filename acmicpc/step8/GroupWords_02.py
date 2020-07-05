answer = 0

# [백준 1316. 그룹 단어 체커]
# - 단어 속의 글자들이 모두 연속으로 이루어진 단어의 갯수를 찾는 프로그램
# * sorted() 의 'key' 속성이 중요!
#     - 특정 기준으로 정렬할 수 있게 정의하는 속성 파라미터
#     - .find 는 해당 list 에서 나오는 순서에 맞게 정렬을 해준다.

for _ in range(int(input())):
    word = input()

    answer += list(word) == sorted(word, key=word.find)

print(answer)
