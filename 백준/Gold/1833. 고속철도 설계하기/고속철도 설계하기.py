import sys
input = sys.stdin.readline
import heapq

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]
def union_parent(x, y):
    x = find_parent(x)
    y = find_parent(y)
    if x<y:
        parent[y] = x
    else:
        parent[x] = y
        
n = int(input())
G = [[] for _ in range(n)]
for i in range(n):
    temp = list(map(int, input().split()))
    G[i] = temp
parent = list(range(n))
edges = []
cnt = 0
res = 0
for i in range(n-1):
    for j in range(i+1, n):
        if G[i][j] < 0:
            res += -G[i][j]
            if find_parent(i) != find_parent(j):
                union_parent(i, j)
                cnt += 1
        else:
            edges.append((G[i][j], i , j))
edges.sort()
res_cnt = 0
res_nodes = []
for key, a, b in edges:
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        res_nodes.append((a+1, b+1))
        cnt += 1
        res_cnt += 1
        res += key
print(res, res_cnt)
for node in res_nodes:
    print(*node)