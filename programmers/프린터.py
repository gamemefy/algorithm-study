# 풀이 1

from collections import decue

def solution(priorities,location):
    answer = 0 # 반환: 원하는 위치에 있는 값(priorities[location])의 인쇄 순서
    d = deque([(v, i) for i, v in enumerate(priorities)])

    while d:
        item = d.popleft()
        if d and max(d)[0] > item[0]:
            d.append(item)
        else: # 가장 왼쪽에 있는 값(item[0])이 가장 큰 값이라는 뜻(같은 값이 여러 개일 가능성 있음)
            answer += 1 
            if item[1] == location: # 가장 왼쪽에 있는 값의 인덱스가 원하는 위치의 값이 맞다면 조건문에서 나오기
                break

    return answer

# 풀이 2

def solution_1(priorities, location):
    queue = [(v, i) for i,v in enumerate(priorities)] # enumerate를 빼먹지 말 것 -> 'Cannot unpack non-iterable int objects'라는 오류 발생했음
    answer = 0

    while True:
        cur = queue.pop(0)
        if any(cur[0] < q[0] for q in queue):
            queue.append(cur)
        
        else:
            answer += 1
            if cur[1] == location:
                break
    
    return answer

    
    
        



    