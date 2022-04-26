# https://programmers.co.kr/learn/courses/30/lessons/92334

from collections import defaultdict

def solution(id_list, report, k): 
    
    answer = list()
    count = defaultdict(int) # 신고 횟수
    user = defaultdict(set) # 신고 리스트
    # {신고한 사람:신고 당한 사람}, 신고 횟수 세기
    for i in report:
        a, b = i.split() 
        if b not in user[a]:
            user[a].add(b)
            count[b] += 1 # 신고당한 횟수
    # 정지기준. 
    for id in id_list:
        result = 0
        for u in user[id]:
            if count[u] >= k:
                result += 1
        answer.append(result)
    return answer