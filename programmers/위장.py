def solution(clothes):
    answer = 1 # 경우의 수 곱셈 위해 1
    kinds = [kind for name, kind in clothes] # 이름은 중복되지 않으므로 종류만 가져와서 사용
    counts = [kinds.count(kind) for kind in set(kinds)] # 종류별로 세서 리스트에 저장. set을 이용해서 중복 불허용 부분 처리
    for cnt in counts: 
        answer *= cnt + 1 # 종류별 개수 + 1 (종류별 옷을 입는 경우의 수 + 안 입는 경우의 수)
    return answer - 1 # 아무것도 입지 않는 경우를 빼줌