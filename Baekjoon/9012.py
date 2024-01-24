# 괄호 - 스택
from sys import stdin

N = int(stdin.readline())

for _ in range(N):
    s = list(stdin.readline().strip())
    # print(s)
    stack = []
    for char in s:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack:
                print("NO")
                break
            stack.pop()
    else:
        if stack:
            print("NO")
        else:
            print("YES")