import sys
input = sys.stdin.readline

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]
def union_parent(x, y):
    x = find_parent(x)
    y = find_parent(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

n = int(input())
edges =[]
for i in range(n):
    cost = int(input())
    edges.append((cost, 0, i+1))
graph = [list(map(int, input().split())) for _ in range(n)]

for i in range(n-1):
    for j in range(i+1, n):
        edges.append((graph[i][j], i+1, j+1))
edges.sort()

res = 0
parent = list(range(n+1))
for cost , a , b in edges:
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        res += cost       

print(res)