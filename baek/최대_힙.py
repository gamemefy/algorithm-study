"""https://www.acmicpc.net/problem/11279
문제:
널리 잘 알려진 자료구조 중 최대 힙이 있다. 최대 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하시오.
    1. 배열에 자연수 x를 넣는다.
    2. 배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거한다.
프로그램은 처음에 비어있는 배열에서 시작하게 된다.
"""

# 틀린 풀이
"""접근법: 연산 개수를 변수로 받고 그걸 for문 길이로 생각해서 sys.stdin.readline() 방법으로 끝까지 받는다. if 자연수: heapq.heappush(heap, 자연수) else: print(heap.pop())
import heapq
import sys
n = int(input())
heap = []
for i in range(n):
    x = sys.stdin.readline()
    if x == 0 :
        if heap:
            heap = sorted(heap)
            print(heap.pop())
        else:
            print(0)
    else:
        heapq.heappush(heap, x)
"""
import heapq
import sys
n = int(input())
heap = []
heapq.heapify(heap)
for _ in range(n):
    x = int(sys.stdin.readline()) # 여기서 int를 안해줘서 런타임 에러가 났음
    if x == 0 and len(heap) == 0:
        print(0)
    elif x == 0:
        print(abs(heapq.heappop(heap)))  
    else:
        heapq.heappush(heap, -x)
    # heapq는 최소 힙 기반이라 일단 -를 붙였고, 빼낼 때 절대값으로 빼내서 최대 힙을 구현함(참고: https://velog.io/@bye9/%EB%B0%B1%EC%A4%80%ED%8C%8C%EC%9D%B4%EC%8D%AC-11279-%EC%B5%9C%EB%8C%80%ED%9E%99)