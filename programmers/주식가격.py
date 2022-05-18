from collections import deque
def solution(prices):
    queue = deque(prices)
    answer = []
    while queue:
        price = queue.popleft()
        time = 0
        for q in queue:
            time += 1 # 일단 다음 번으로 넘어가면 1을 세어 줘야 함
            if price > q: #
                break
            
        answer += [time] # answer.append(time)
    return answer