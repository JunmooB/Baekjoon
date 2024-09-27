import sys
input = sys.stdin.readline

from collections import deque


k = int(input())
w , h = map(int, input().split())
visited = [[[0] * (w) for _ in range(h)] for _ in range(k+1)]
graph =[]
for _ in range(h):
    temp = list(map(int, input().split()))
    graph.append(temp)
    
    
# [k , x, y]    
q = deque([[0,0,0]])

def bfs():
    while q:        
        z , x, y = q.popleft()
        if x == h-1 and y == w-1:
            return visited[z][x][y]
        dx = [0, -1, 0, 1,  -1, -2, -2, -1, 1, 2, 2, 1]
        dy = [-1, 0, 1, 0,  -2, -1, 1, 2, 2, 1, -1 ,-2]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]        
            if 0<=nx<h and 0<=ny<w and graph[nx][ny] == 0:
                if visited[z][nx][ny] == 0:
                    q.append([z, nx, ny])
                    visited[z][nx][ny] = visited[z][x][y] + 1
        if z < k:
            for i in range(4,12):
                nx = x + dx[i]
                ny = y + dy[i]        
                if 0<=nx<h and 0<=ny<w and graph[nx][ny] == 0:
                    if visited[z+1][nx][ny] == 0:
                        q.append([z+1, nx, ny])
                        visited[z+1][nx][ny] = visited[z][x][y] + 1
    return -1            
    
print(bfs())
