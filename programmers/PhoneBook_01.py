def solution(phone_book):
    # [프로그래머스 문제 : 전화번호 목록]
    # - zip 내장함수를 통해서 첫번째 index 요소 비교
    phone_book = sorted(phone_book)

    for p1, p2 in zip(phone_book, phone_book[1:]):
        print(p1, '<->', p2)
        if p2.startswith(p1):
            return False
    return True


phone_book = ['119', '97674223', '1195524421']
print(solution(phone_book))