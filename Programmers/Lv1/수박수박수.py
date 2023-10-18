def solution(n):
    ans = []
    for i in range(1,n+1):
        if i % 2 == 0: # 짝수
            ans.append('박')
        else:
            ans.append('수')
    ans = ''.join(ans)
    # print(ans)
    return ans

solution(3)