import sys

n = int(sys.stdin.readline()) # 입력 개수
x = list(map(int, input().split()))

print(min(x), max(x))