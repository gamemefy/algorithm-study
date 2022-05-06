import math

def convert(n, k):
    s = ''
    while n: # n이 0이 아닐 때
        s += str(n%k) # k로 나눈 나머지를 순서대로 저장(일의자리수 부터 오름차순)
        n //= k # n을 k로 나눈 몫을 n에 저장
    return s[::-1] # 뒤집어서 출력

def isPrime(x):
    if x == 1: return False
    i = 2
    while i <= math.floor(math.sqrt(x)): # 에라토스테네스의 체 이용
        if x%i ==0: return False
        i+=1
    return True

def solution(n, k):
    answer = 0
    x = convert(n, k)
    for i in x.split('0'):
        if not i: continue # '' 인 경우 무시하고 넘어감
        if isPrime(int(i)): answer += 1
    return answer