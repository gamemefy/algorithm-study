def solution(genres, plays):
    answer = []
    dict_plays = {} # 장르별 재생 횟수
    dict_idx_plays = {} # 장르별 (고유번호, 재생 횟수)
    
    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in dict_plays:
            dict_plays[g] = p
        else:
            dict_plays[g] += p

        if g not in dict_idx_plays:
            dict_idx_plays[g] = [(i, p)]
        else:
            dict_idx_plays[g] += [(i, p)]

    for (g, p) in sorted(dict_plays.items(), key = lambda x:x[1], reverse = True): # .items() 빼먹으면 오류
        for (i, j) in sorted(dict_idx_plays[g], key = lambda x:x[1], reverse = True)[:2]:
            answer.append(i)
    return answer


