import sys
input = sys.stdin.readline

from collections import deque

def bfs(x, y, group_idx):
    q = deque([(x, y)])
    visited[x][y] = True
    zero_cnts[x][y] = group_idx
    cnt = 1
    while q:
        x , y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if not visited[nx][ny] and matrix[nx][ny] == 0:
                    cnt += 1
                    visited[nx][ny] = True
                    zero_cnts[nx][ny] = group_idx
                    q.append((nx, ny))
                
    return cnt % 10
        

n , m = map(int, input().split())
matrix = [list(map(int, input().strip())) for _ in range(n)]
zero_cnts = [[0] * m for _ in range(n)]
group_num = 1
groups = {}
groups[0] = 0

visited = [[False] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0 and not visited[i][j]:
            val = bfs(i, j, group_num)
            groups[group_num] = val
            group_num += 1
            
res = []
for i in range(n):
    temp_res = []
    for j in range(m):
        if matrix[i][j] == 0:
            temp_res.append(0)
        else:
            zero_list = []
            temp_cnt = 1
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0<=nx<n and 0<=ny<m:
                    if not zero_cnts[nx][ny] in zero_list:
                        zero_list.append(zero_cnts[nx][ny])
            for zero in zero_list:
                temp_cnt += groups[zero]
            temp_cnt %= 10
            temp_res.append(temp_cnt)
    res.append(temp_res)
for r in res:
    print(''.join(map(str, r)))