#스택
def rotate(s, n):
    return s[n:] + s[:n]

def solution(s):
    answer = 0
    for x in range(len(s)):
        rotated = rotate(s, x)
        stack = []
        for i in rotated:
            if i in ["(", "[", "{"]:
                stack.append(i)
            else:
                if len(stack) == 0:
                    break
                if i == ")" and stack[-1] == "(":
                    stack.pop()
                elif i == "]" and stack[-1] == "[":
                    stack.pop()
                elif i == "}" and stack[-1] == "{":
                    stack.pop()
                else:
                    break
        else:
            if len(stack) == 0:
                answer += 1
    return answer

print(solution("[](){}"))
print(solution("}]()[{"))
