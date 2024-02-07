# DFS와 BFS_DFS/BFS
import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())
graph = [[0] * (N + 1) for _ in range(N + 1)] 
visit_list = [0] * (N + 1)
visit_list2 = [0] * (N + 1)

for _ in range(M): # 연결된 정점 입력
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = 1

def bfs(V):
    q = deque()
    q.append(V)       
    visit_list[V] = 1   
    while q:
        V = q.popleft()
        print(V, end = " ")
        for i in range(1, N + 1):
            if visit_list[i] == 0 and graph[V][i] == 1:
                q.append(i)
                visit_list[i] = 1

def dfs(V):
    visit_list2[V] = 1        
    print(V, end = " ")
    for i in range(1, N + 1):
        if visit_list2[i] == 0 and graph[V][i] == 1:
            dfs(i)

dfs(V)
print()
bfs(V)