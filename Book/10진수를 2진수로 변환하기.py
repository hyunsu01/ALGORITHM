# 스택
def solution(decimal):
    stack = []
    while decimal != 0:
        stack.append(str(decimal % 2))
        decimal = decimal // 2

    binary = ''.join(stack[::-1])
    return binary


print(solution(10))
print(solution(27))
print(solution(12345))