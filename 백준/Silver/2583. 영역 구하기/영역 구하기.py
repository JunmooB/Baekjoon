import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def dfs(x,y):
    global Sum
    Sum += 1
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m:
            if matrix[nx][ny] == 0:
                matrix[nx][ny] = 1
                dfs(nx,ny)


n , m , k = map(int, input().split())
matrix = [[0] * (m) for _ in range(n)]
for _ in range(k):
    x_min , y_min, x_max, y_max = map(int, input().split())
    for x in range(x_min, x_max):
        for y in range(y_min, y_max):
            matrix[y][x] = 1

res = 0
res_list =[]
for a in range(n):
    for b in range(m):         
        if matrix[a][b] == 0:
            matrix[a][b] = 1
            res+=1
            Sum = 0
            dfs(a,b)
            res_list.append(Sum)

print(res)
res_list.sort()
for res_li in res_list:
    print(res_li, end=' ')