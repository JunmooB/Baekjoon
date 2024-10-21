import sys
input = sys.stdin.readline

def func_max_checker(graph):
    res = 0
    for i in range(n):
        temp = 1
        for j in range(n-1):
            if graph[i][j] == graph[i][j+1]:
                temp += 1
            else:
                temp = 1
            if temp > res:
                res = temp    

    for i in range(n):
        temp = 1
        for j in range(n-1):
            if graph[j][i] == graph[j+1][i]:
                temp += 1
            else:
                temp = 1
            if temp > res:
                res = temp
    return res
n = int(input())
boards = [list(map(str, input().strip())) for _ in range(n)]

dx = [1,0]
dy = [0,1]
result = 0
for i in range(n):
    for j in range(n):
        for k in range(2):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0<=nx<n and 0<=ny<n:
                if boards[i][j] != boards[nx][ny]:
                    boards[i][j] , boards[nx][ny] = boards[nx][ny], boards[i][j]
                    val = func_max_checker(boards)
                    if val > result: result = val
                    boards[i][j] , boards[nx][ny] = boards[nx][ny], boards[i][j]
print(result)                    