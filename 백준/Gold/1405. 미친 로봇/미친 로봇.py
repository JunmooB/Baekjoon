import sys
input = sys.stdin.readline

def dfs(x, y) :
    global cnt
    global result
    if cnt == n :        
        temp = 1
        for i in range(4):
            temp *= proba[i] ** visited[i]
        result += temp         
        return

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0 ,0]
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx <(2*n+1) and 0<=ny<(2*n+1) :
            if graph[nx][ny] == 1:
                continue
            else :
                cnt += 1
                graph[nx][ny] +=1
                visited[i] += 1
                dfs(nx , ny)
                cnt -=1
                graph[nx][ny] -=1
                visited[i] -=1   

cnt = 0
data = list(map(int, input().split()))
n = data[0]

graph = [[0] * (2*n+1) for _ in range(2*n+1)]
graph[n][n]= 1

proba = []
for i in range(1,5):
    proba.append(data[i] /100)

result = 0
visited =[0, 0, 0, 0]
dfs(n,n)
print(result)