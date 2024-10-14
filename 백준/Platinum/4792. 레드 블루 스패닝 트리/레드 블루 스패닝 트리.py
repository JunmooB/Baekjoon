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

while True:
    n , m , k = map(int, input().split())
    if n == 0 and m == 0 and k == 0: break
    min_edges , max_edges = [], []
    
    for _ in range(m):
        color , a , b = map(str, input().split())
        # min blue
        if color == 'B':
            min_edges.append((0, int(a), int(b)))
            max_edges.append((1, int(a), int(b)))
        else:
            min_edges.append((1, int(a), int(b)))
            max_edges.append((0, int(a), int(b)))
    min_edges.sort()
    max_edges.sort()
    parent = list(range(n+1))
    min_res = 0
    for key, a, b in min_edges:
        if find_parent(a) != find_parent(b):
            union_parent(a, b)
            if key == 0:
                min_res += 1
    parent = list(range(n+1))
    max_res = 0
    for key, a, b in max_edges:
        if find_parent(a) != find_parent(b):
            union_parent(a, b)
            if key == 1:
                max_res += 1
    if max_res <= k <= min_res:
        print(1)
    else:
        print(0)