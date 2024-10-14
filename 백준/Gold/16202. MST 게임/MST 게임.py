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
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

n , m, k = map(int, input().split())
edges = []
for i in range(m):
    x, y = map(int, input().split())
    edges.append((i+1, x, y))
    
results = []
for i in range(k):
    parent = list(range(n+1))
    res , cnt = 0 , 0
    for key, a, b in edges:
        if find_parent(a) != find_parent(b):
            union_parent(a, b)
            res += key
            cnt += 1
    if cnt == n-1:
        results.append(res)
    else:
        for j in range(i, k):
            results.append(0)
        break
    edges.pop(0)
    
print(*results)