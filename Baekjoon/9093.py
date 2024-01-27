# 단어 뒤집기 - 스택
N = int(input())

for _ in range(N):
    string = input().split()
    stack = []
    for i in string:
        for k in i:
            stack.append(k)
        while stack:
            print(stack.pop(), end="")
        print(" ", end="")
    print()

"""
for i in range(N):
    a = input().split()
    for j in a:
        print(j[::-1], end=' ')
"""