import sys
input = sys.stdin.readline

n , m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, m):
    graph[0][i] += graph[0][i-1]

for i in range(1, n):
    left , right = [], []
    temp = graph[i-1][0] + graph[i][0]
    left.append(temp)
    for j in range(1, m):
        if temp >= graph[i-1][j]:
            temp = temp + graph[i][j]
            left.append(temp)
        else:
            temp = graph[i-1][j] + graph[i][j]
            left.append(temp)

    temp = graph[i-1][m-1] + graph[i][m-1]
    right.append(temp)
    for j in range(m-2, -1, -1):
        if temp >= graph[i-1][j]:
            temp = temp + graph[i][j]
            right.append(temp)
        else:
            temp = graph[i-1][j] + graph[i][j]
            right.append(temp)    
    for k in range(len(graph[i])):
        if left[k] >= right[m-1-k]:
            graph[i][k] = left[k]
        else:
            graph[i][k] = right[m-1-k]

print(graph[n-1][m-1])