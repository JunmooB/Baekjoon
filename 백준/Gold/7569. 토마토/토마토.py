import sys
input = sys.stdin.readline

from collections import deque
   

m , n , h = map(int, input().split())
matrix =[]
q = deque([])
for i in range(h):
    temp_list =[]
    for j in range(n):
        temp = list(map(int, input().split()))
        for ind, value in enumerate(temp):
            if value == 1:
                q.append([i,j,ind])
        temp_list.append(temp)
    matrix.append(temp_list)

dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]
while q:    
    x, y, z = q.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if 0<=nx<h and 0<=ny<n and 0<=nz<m:
            if matrix[nx][ny][nz] == 0 :
                q.append([nx, ny, nz])
                matrix[nx][ny][nz] = matrix[x][y][z] + 1

res = 0
for mat in matrix:
    for ma in mat:
        for val in ma:
            if val == 0:
                print(-1)
                exit(0)
        res = max(max(ma),res)
print(res-1)