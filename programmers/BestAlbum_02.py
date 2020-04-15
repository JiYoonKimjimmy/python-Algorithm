def solution(genres, plays):
    answer = []
    genres_dic = {}
    genres_list = []

    for i in range(len(genres)):
        if (genres[i] not in genres_dic):
            genres_dic[genres[i]] = []
        genres_dic[genres[i]].append([i, plays[i]])

    for genre in genres_dic:
        genres_dic[genre].sort(key=lambda g:g[1], reverse=True)
        genres_list.append([genre, sum([play for _, play in genres_dic[genre]])])

    genres_list.sort(key=lambda g:g[1], reverse=True)
    print('genres_dic : ', genres_dic)
    print('genres_list : ', genres_list)

    for genre, _ in genres_list:
        answer.extend([x[0] for x in genres_dic[genre][:2]])

    return answer


genres = ['classic', 'pop', 'classic', 'classic', 'pop']
plays = [500, 600, 150, 800, 2500]
print('answer : ', solution(genres, plays))