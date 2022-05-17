def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length # 다리 길이만한 리스트 생성
    while bridge: # 다리 길이가 모두 0이 아닌 동안
        answer += 1 # 시간이 1 지남
        bridge.pop(0) # 가장 앞에 있는 트럭 또는 공간이 다리를 통과
        if truck_weights: # 대기열에 트럭이 있다면
            if sum(bridge) + truck_weights[0] <= weight: # 다리 위 모든 트럭 하중 합과 첫번쨰 대기 트럭 하중의 합이 최대 하중 이하이면
                bridge.append(truck_weights.pop(0))
            else: # 최대 하중을 넘기면
                bridge.append(0) # 0을 붙여서 아무 트럭도 올라오지 않았음을 나타냄

    return answer
    