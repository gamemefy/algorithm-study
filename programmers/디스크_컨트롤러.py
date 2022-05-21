import heapq
def solution(jobs):
    # 입력: jobs = [[요청시간, 작업 소요 시간]] 형태
    # 작업 소요 시간 평균이 가장 작을 때 그 값
    # 작업 소요 시간의 평균이 가장 적으려면 범위 내에서 작업 소요 시간이 적은 순서대로 정렬해서 순서대로 수행해야 함 -> 최소 힙(heapq)
    # jobs는 그대로 두고 heap을 생성할 것
    heap = []
    total = 0 # 평균을 구하기 위해 구하는 시간의 총합
    n = len(jobs) 
    i = 0 # jobs의 모든 원소를 돌았는지 확인하기 위한 인덱스. [0, n-1]
    now = 0 # 현재 작업 종료 시간 (다음 작업 시간이 아닐 수 있음. 작업이 끝난 시점에 요청된 것이 아무것도 없는 경우)
    start = -1 # 현재 작업 시작 시간

    while i < n:
            for j in jobs:
                if start < j[0] <= now: # 요청 시간이 이전 작업 수행 사이에 들어왔다면
                    heapq.heappush(heap, [j[1], j[0]]) # 작업 시간 기준으로 힙 생성하기 위해 원소 각각 내부 원소 두 개의 위치를 바꿈
            if heap: 
            # 힙에 어떤 원소가 들어왔다면(즉 start ~ now 범위 동안 요청이 들어왔다면)
                current = heapq.heappop(heap) # 현재 작업
                start = now # 현재 시간이 현재 작업의 시작 시간
                now += current[0] # 현재 작업의 소요 시간을 현재 시각에 더해서 저장
                total += now - current[1] # 현재 작업이 끝나는 시간 - 요청 시간
                i += 1 # heap에서 한 가지 원소를 제거했으므로 인덱스 하나 추가
            else:
                now += 1 # 현재 시간만 하나 더 지나감
    return total//n 