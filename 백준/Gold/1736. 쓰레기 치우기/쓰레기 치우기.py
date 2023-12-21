import sys
input = sys.stdin.readline

def cond_escape(graph):
    cnt = 0
    for row in graph:
        cnt += row.count(1)
    if cnt == 0:
        return True

def cleaning_robot(row, col):
    while True: 
        if graph[row][col:].count(1):
            temp = graph[row][col:].index(1)
            temp += col
            if temp >= col:
                graph[row][temp] = 0
                col = temp
        else:
            row += 1
        if (row == n-1 and col == m-1) or (row == n-1 and graph[row][col:].count(1) == 0):
            graph[row][col] = 0
            break
n , m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
result = 0
graph[0][0] = 0

while True:
    result += 1
    cleaning_robot(0,0)    
    if cond_escape(graph):
        print(result)
        break