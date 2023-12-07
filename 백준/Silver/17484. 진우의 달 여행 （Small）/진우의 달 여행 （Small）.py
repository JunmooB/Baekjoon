import sys
input = sys.stdin.readline

n , m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 1 , 1]
dy = [-1, 0, 1]
result = 1e9
cnt = 0
def dfs(x, y, type, cnt):
    global result
    cnt += graph[x][y]
    
    if x == n-1:
        if result > cnt:
            result = cnt
            return result
    for i in range(3):
        if i == type:
            continue
        else:
            nx = x + 1
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                dfs(nx, ny, i, cnt)
                # cnt -= graph[nx][ny]

for col in range(m):
    for t in range(3):
        dfs(0,col, t, 0)
print(result)