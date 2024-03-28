# 스택
def solution(arr):
    stack = []
    for s in arr:
        if s == "(":
            stack.append(s)
        elif s == ")":
            if not stack:
                return False
            else:
                stack.pop()
    if stack: # 남아있다면
        return False
    else:
        return True
    
print(solution("()()"))
print(solution("(()"))