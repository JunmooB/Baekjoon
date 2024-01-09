import sys
input = sys.stdin.readline

n = int(input())

matrix = []
for _ in range(n):
    x , y = map(int, input().split())
    matrix.append([x, y])
matrix.sort()
for res in matrix:
    print(res[0], res[1])