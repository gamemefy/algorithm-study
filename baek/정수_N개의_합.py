# 풀이 1
def solve(a):
    return sum(a) # 그냥 이렇게 하면 리스트 합이 구해진다. 어렵게 생각하지 말 것

# 풀이 2
def solve(a):
    ans = 0
    for num in a:
        ans += num
    return ans
