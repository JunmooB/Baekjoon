import sys
input = sys.stdin.readline

from collections import deque

def bfs(a, b):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    queue = deque()
    queue.append((a,b))
    while queue:
        x , y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m :
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx,ny))    

n , m = map(int, input().split())
graph = []
for _ in range(n):
    temp = list(map(int, input().strip()))
    graph.append(temp)
bfs(0, 0)
print(graph[n-1][m-1])