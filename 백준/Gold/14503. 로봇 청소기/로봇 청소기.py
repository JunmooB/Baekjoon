import sys
input = sys.stdin.readline

from collections import deque


n , m = map(int, input().split())
r , c , d = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
res = 0
while True:
    if matrix[r][c] == 0:
        res += 1
        matrix[r][c] = 2
    checker = 0
    for i in range(4):
        nx = r + dx[i]
        ny = c + dy[i]
        if matrix[nx][ny] != 0:
            checker += 1
        else:
            pass
            # 청소할 공간 있으면
    if checker == 4:
        dir_back = (d + 2) % 4
        nx = r + dx[dir_back]
        ny = c + dy[dir_back]
        if 0<=nx<n and 0<=ny<m:
            if matrix[nx][ny] == 1:
                break
            else:
                r = nx
                c = ny
    else:
        d = (d+3) % 4
        nx = r + dx[d]
        ny = c + dy[d]
        if matrix[nx][ny] == 0 :
            r = nx
            c = ny
print(res)