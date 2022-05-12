import sys
N = int(sys.stdin.readline()) # (입력 첫줄) 입력 개수를 받아 정수로 변환
stack = []

for _ in range(N):
    i = sys.stdin.readline().split() # 줄마다 들어오는 입력을 띄어쓰기 기준으로 나눔
    call = i[0] # 명령어
    
    if call == 'push':
        stack.append(int(i[1])) # 기본적으로 문자열이므로 정수형으로 변환
    
    elif call == 'pop':
        if not stack: # 스택이 비었을 때
            print(-1)
        else:
            print(stack.pop())
    
    elif call == 'size':
        print(len(stack))
    
    elif call == 'top':
        if not stack: # 스택이 비었을 때
            print(-1)
        else:
            print(stack[-1]) # 스택의 맨 위이므로 pop 하면 빠져나갈 리스트의 마지막 원소여야 함
    
    elif call == 'empty':
        if not stack: # 스택이 비었을 때
            print(1)
        else:
            print(0)       

    