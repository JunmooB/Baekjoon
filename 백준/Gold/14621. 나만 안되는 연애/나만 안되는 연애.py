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

n , m = map(int, input().split())
checker = list(map(str, input().split()))
edges = []
parent = list(range(n+1))
for _ in range(m):
    a , b , c = map(int, input().split())
    edges.append([c, a, b])
edges.sort()
cnt = 0
res = 0
for key , a, b in edges:
    if checker[a-1] == checker[b-1]: continue
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        res += key
        cnt += 1
        
if cnt == n-1:
    print(res)
else:
    print(-1)
