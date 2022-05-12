N = int(input()) # 왜 숫자의 개수를 줬을까에 대해 고민하다보니, 문자열의 길이를 준 것 -> for문을 쓰라는 것이라고 이해하게 됨
x = input()
answer = 0
for i in range(N):
    answer += x[i]

print(answer)