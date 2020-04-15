def solution(genres, plays):
    # [프로그래머스 문제 : 베스트 앨범]
    # - 장르별 합계 재생수와 (genre, play, index) class 를 이용하여
    # - 가장 큰 재생수를 가진 장르부터 2개씩 pop 하여 answer 에 append
    answer = []
    dic = {}            # 장르별 재생수 합계 dic
    album_list = []     # album class list
    for i in range(len(genres)):
        dic[genres[i]] = dic.get(genres[i], 0) + plays[i]
        album_list.append(album(genres[i], plays[i], i))

    # 재생수순으로 sort
    dic = sorted(dic.items(), key=lambda dic:dic[1], reverse=True)

    # album list sort
    album_list = sorted(album_list, reverse=True)

    print('dic : ', dic)

    while len(dic) > 0:
        play_genre = dic.pop(0)

        cnt = 0
        for ab in album_list:
            if play_genre[0] == ab.genre:
                answer.append(ab.track)
                cnt += 1
            if cnt == 2:
                break

    return answer


class album:
    def __init__(self, genre, play, track):
        self.genre = genre
        self.play = play
        self.track = track

    def __lt__(self, other):
        return self.play < other.play

    def __le__(self, other):
        return self.play <= other.play

    def __gt__(self, other):
        return self.play > other.play

    def __ge__(self, other):
        return self.play >= other.play

    def __eq__(self, other):
        return self.play == other.play

    def __ne__(self, other):
        return self.play != other.play


genres = ['classic', 'pop', 'classic', 'classic', 'pop']
plays = [500, 600, 150, 800, 2500]
print('answer : ', solution(genres, plays))
