import sys
input = sys.stdin.readline

from collections import deque

def bfs(_start, _target):
    q = deque([_start])
    while q:
        x , y = q.popleft()
        if x == _target[0] and y == _target[1]:
            print(graph[x][y]-1)
            break
        else:
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<n and 0<=ny<n:
                    if graph[nx][ny] == 0:
                        graph[nx][ny] += graph[x][y] + 1
                        q.append([nx, ny])
        
    

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]

t = int(input())
for _ in range(t):
    n = int(input())
    graph = [[0] * (n) for _ in range(n)]
    start = list(map(int, input().split()))
    target = list(map(int, input().split()))
    graph[start[0]][start[1]] = 1
    bfs(start, target)