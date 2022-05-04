# 2 ~ n까지 수 중 n의 제곱근까지의 자연수 중 소수의 배수를 제거하고, 그 소수들과 나머지 수를 합하면 
# 1 ~ n까지 모든 소수임
import math

def is_prime(x):
    for i in range(2, math.ceil(math.sqrt(x))): # x = 200이면 제곱근은 14.aaa 이므로 여기서 올림
        if x % i == 0: 
            return False # 나눠떨어지면 소수가 아님
    return True # 나눠떨어지지 않았으므로 소수
    
