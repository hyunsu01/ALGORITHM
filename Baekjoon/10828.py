# 스택/큐
from sys import stdin

N = int(stdin.readline())
ans = []
for i in range(N):
    words = stdin.readline().split()
    # print(words)
    if words[0] == 'push':
        ans.append(int(words[1]))
    elif words[0] == 'pop':
        if len(ans)==0:
            print(-1)
        else:
            print(ans.pop())
    elif words[0] == 'size':
        print(len(ans))
    elif words[0] == 'empty':
        if len(ans)==0:
            print(1)
        else:
            print(0)
    elif words[0] == 'top':
        if len(ans)==0:
            print(-1)
        else:
            print(ans[-1])