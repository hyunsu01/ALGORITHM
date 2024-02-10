# 연결 요소의 개수 _ BFS / DFS
from collections import deque
import sys
sys.setrecursionlimit(10000)

def bfs(graph, x, visited):
    queue = deque([x])
    visited[x] = True

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

count = 0
visited = [False] * (n+1)
for i in range(1, n+1):
    if not visited[i]:
        bfs(graph, i, visited)
        count += 1

print(count)