# 유기농 배추 _ BFS / DFS
from collections import deque
import sys

T = int(sys.stdin.readline())
graph = []
count = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, a, b):
    queue = deque()
    queue.append((a,b))
    graph[a][b] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >=N or ny < 0 or ny >= M:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
    return

for _ in range(T):
    cnt = 0
    N, M, K = map(int, sys.stdin.readline().split())
    graph = [[0]*M for _ in range(N)]

    for j in range(K):
        x, y = map(int, sys.stdin.readline().split())
        graph[x][y] = 1

    for a in range(N):
        for b in range(M):
            if graph[a][b] == 1:
                bfs(graph, a, b)
                cnt += 1
    print(cnt)