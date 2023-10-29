import math

def solution(balls, share):
    ans = math.comb(balls, share)
    print(ans)
    return ans

solution(3,2)