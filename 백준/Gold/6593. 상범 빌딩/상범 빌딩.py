import sys
input = sys.stdin.readline

from collections import deque

while True:
    l , r , c = map(int, input().split())
    if l == 0 and r == 0 and c == 0:
        break
    visited =[[[0]*(c) for _ in range(r)] for __ in range(l)]
    graph = []
    for _ in range(l):
        temp_list=[]
        for i in range(r):
            temp = list(map(str, input().strip()))
            for ind, value in enumerate(temp):
                if value == 'S':
                    start = [_ , i ,ind]
                    visited[_][i][ind] = 1
                elif value == 'E':
                    end = [_ , i , ind]
            temp_list.append(temp)
        # temp = [list(map(str, input().strip())) for __ in range(r)]
        graph.append(temp_list)
        input()
        
    dx = [-1,1,0,0,0,0]
    dy = [0,0,-1,1,0,0]
    dz = [0,0,0,0,-1,1]
    q = deque([start])
    checker = True
    while q:
        now = q.popleft()
        if now == end:
            checker = False
            res = visited[now[0]][now[1]][now[2]]-1
            print(f"Escaped in {res} minute(s).")
            break
        else:
            x , y , z = now[0], now[1], now[2]
            for i in range(6):
                nx = x + dx[i]
                ny = y + dy[i]
                nz = z + dz[i]
                if 0<=nx<l and 0<=ny<r and 0<=nz<c:
                    if graph[nx][ny][nz] != '#' and visited[nx][ny][nz] == 0:
                        visited[nx][ny][nz] = visited[x][y][z] + 1
                        q.append([nx, ny, nz])
    if checker:
        print("Trapped!")
                    
