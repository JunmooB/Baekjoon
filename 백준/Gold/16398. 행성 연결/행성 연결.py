import sys
input = sys.stdin.readline

import heapq

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
parent = list(range(n))
graph = [list(map(int, input().split())) for _ in range(n)]
edges = []
for i in range(n-1):
    for j in range(i+1,n):
        edges.append([graph[i][j], i, j])
edges.sort()
res = 0
for key, a, b in edges:
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        res += key
print(res)