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

n , m , k = map(int, input().split())

elec_list = list(map(int, input().split()))
first_parent = min(elec_list)
parent = list(range(n+1))
for elec in elec_list:
    parent[elec] = first_parent

edges =[]
for i in range(m):
    a, b, c = map(int, input().split())
    edges.append([c, a, b])
edges.sort()
res = 0
for key, a, b in edges:
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        res += key
print(res)
