import sys
input = sys.stdin.readline

from collections import deque

m, n  = map(int, input().split())
miro = [list(map(int, input().strip())) for _ in range(n)]
dist = [[int(1e9)] * (m) for _ in range(n)]

q = deque([(0,0)])
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
dist[0][0] = 0
while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m:
            if miro[nx][ny] == 1:
                if dist[x][y] + 1 < dist[nx][ny]:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
            else:
                if dist[x][y] < dist[nx][ny]:
                    dist[nx][ny] = dist[x][y]
                    q.append((nx, ny))
print(dist[n-1][m-1])