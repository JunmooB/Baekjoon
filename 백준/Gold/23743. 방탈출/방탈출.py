import sys
input = sys.stdin.readline

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(x , y):
    x = find_parent(x)
    y = find_parent(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

n , m = map(int, input().split())
edges = []
for _ in range(m):
    a , b , c = map(int, input().split())
    edges.append((c , a , b))
exits = list(map(int, input().split()))
for i , exit in enumerate(exits):
    edges.append((exit, 0, i+1))
    
edges.sort()
parent = list(range(n+1))
cnt , res = 0 , 0
for key , a , b in edges:
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        cnt += 1
        res += key       

print(res)