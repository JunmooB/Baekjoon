import sys
input = sys.stdin.readline

from collections import deque
from itertools import combinations

def bfs(x, y):
    q = deque([(x, y)])
    cnt = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                if matrix[nx][ny] == 0 :
                    q.append((nx, ny))
                    visited[nx][ny] =True
                    cnt += 1
    return cnt
                
                
    
dx = [-1, 1, 0 , 0]
dy = [0, 0, -1, 1]

n , m = map(int, input().split())
matrix = []
blank_list = []
virus_list = []
zero_cnt = 0
for i in range(n):
    temp = list(map(int, input().split()))
    matrix.append(temp)
    for ind, t in enumerate(temp):
        if t == 0:
            blank_list.append((i, ind))
            zero_cnt += 1
        elif t==2:
            virus_list.append((i, ind))
        
combi = list(combinations(blank_list, 3))
res = 0
for com in combi:
    case_cnt = 0
    visited = [[False] * m for _ in range(n)]
    for a, b in com:
        matrix[a][b] = 1
    for virus_x, virus_y in virus_list:        
        case_cnt += bfs(virus_x, virus_y)
    temp_res = zero_cnt - case_cnt - 3
    res = max(temp_res, res)
    for a, b in com:
        matrix[a][b] = 0
print(res)