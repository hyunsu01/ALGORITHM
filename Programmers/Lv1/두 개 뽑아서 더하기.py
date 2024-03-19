# 배열
def solution(numbers):
    ans = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            ans.append(numbers[i] + numbers[j])
    ans = sorted(list(set(ans)))
    return ans

solution([2,1,3,4,1])