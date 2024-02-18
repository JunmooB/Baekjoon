import sys
input = sys.stdin.readline

from collections import deque  
def bfs(x, y, temp_cnt):
    queue = deque()
    queue.append([x, y])
    temp_cnt += 1
    while queue:
        x , y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == 1:
                    queue.append([nx,ny])
                    graph[nx][ny] = 0
                    temp_cnt += 1
    return temp_cnt
        


n , m = map(int, input().split())
pictures = []
graph = []
for i in range(n):
    temps = list(map(int, input().split()))
    for ind, temp in enumerate(temps):
        if temp == 1:
            pictures.append([i, ind])
    graph.append(temps)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

res_nums = 0
max_area = 0
for picture in pictures:
    a, b = picture[0] , picture[1]
    if graph[a][b] == 1:
        graph[a][b] = 0
        res_nums += 1
        temp_cnt = 0
        cnt = bfs(a, b, temp_cnt)

        if cnt > max_area:
            max_area = cnt
print(res_nums)
print(max_area)