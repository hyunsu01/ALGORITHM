def solution(rsp):
    # S = 2 R = 0 P = 5
    ans = []
    for hand in rsp:
        if hand == "2":
            ans.append("0")
        elif hand == "0":
            ans.append("5")
        elif hand == "5":
            ans.append("2")
    ans = ''.join(ans)
    print(ans)
    return ans

solution("2")
solution("205")