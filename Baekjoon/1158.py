# 스택/큐
# 요세푸스 문제
from collections import deque
from sys import stdin

N, K = map(int, stdin.readline().split())
queue = deque()

for num in range(1, N+1):
    queue.append(num)

ans = []
for i in range(len(queue)):
    queue.rotate(-(K-1))
    # print(queue)
    ans.append(str(queue.popleft()))

print("<", ", ".join(ans), ">", sep = '')