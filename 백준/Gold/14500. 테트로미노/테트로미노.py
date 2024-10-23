import sys
input = sys.stdin.readline


def general_dfs(x, y, val, cnt ):
    global res
    if cnt == 4:
        res = max(res, val)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m:
            if not visited[nx][ny]:
                visited[nx][ny] = True
                general_dfs(nx, ny, val + graph[nx][ny], cnt+1)
                visited[nx][ny] = False
def irre_dfs(x, y):
    global res
    cnt = 0
    temp_min = 1e9
    val = graph[x][y]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m:
            cnt += 1
            val += graph[nx][ny]
            temp_min = min(temp_min, graph[nx][ny])
    if cnt == 3:
        res = max(res, val)
        return
    if cnt == 4:
        val -= temp_min
        res = max(res, val)
        return


n , m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * (m) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

res = 0

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        general_dfs(i,j, graph[i][j], 1 )
        irre_dfs(i,j)
        visited[i][j] = False
print(res)