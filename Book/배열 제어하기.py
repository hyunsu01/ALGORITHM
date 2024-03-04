def solution(arr):
    ans = list(set(arr))
    ans.sort(reverse = True)
    print(ans)
    return ans

solution([4, 2, 2, 1, 3, 4])