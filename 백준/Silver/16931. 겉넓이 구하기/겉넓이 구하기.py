import sys
input = sys.stdin.readline

n , m = map(int, input().split())
cubes = [list(map(int, input().split())) for _ in range(n)]

front_cnt = 0
for i in range(n):
    front_temp = cubes[i][0]
    for j in range(1, m):
        if cubes[i][j] > cubes[i][j-1]:
            front_temp += cubes[i][j] - cubes[i][j-1]
    front_cnt += front_temp

side_cnt = 0
for i in range(m):
    side_temp = cubes[0][i]
    for j in range(1, n):
        if cubes[j][i] > cubes[j-1][i]:
            side_temp += cubes[j][i] - cubes[j-1][i]
    side_cnt += side_temp

res = 2 * (front_cnt + side_cnt + n*m)
print(res)