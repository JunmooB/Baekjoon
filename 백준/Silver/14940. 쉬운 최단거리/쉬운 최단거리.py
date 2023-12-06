import sys
input = sys.stdin.readline

from collections import deque

n , m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * (m) for _ in range(n)]

for i in range(n):
    for j in range(m) :
        if graph[i][j] == 2:
            target = [i, j]
            graph[i][j] = 0
            visited[i][j] = True

dx = [0, 0 ,-1, 1]
dy = [1, -1, 0, 0]

queue = deque([target])
while queue:
    v= queue.popleft()
    for i in range(4):
        nx = v[0] + dx[i]
        ny = v[1] + dy[i]
        if 0<=nx<n and 0<=ny<m:
            if visited[nx][ny] == False and graph[nx][ny] == 1:
                graph[nx][ny] = graph[v[0]][v[1]] + 1
                visited[nx][ny] = True
                queue.append((nx, ny))
            elif visited[nx][ny] == False and graph[nx][ny] == 0:
                visited[nx][ny] = True

for i in range(n):
    for j in range(m):
        if visited[i][j] == True:
            print(graph[i][j], end=' ')
        elif visited[i][j] == False and graph[i][j] == 0:
            print(0, end= ' ')
        elif visited[i][j] == False and graph[i][j] == 1:
            print(-1, end=' ')
    print()