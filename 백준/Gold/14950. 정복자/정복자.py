import sys
input = sys.stdin.readline

import heapq

def prim(start, weight):
    visited = [False] *(n+1)
    q = [(weight, start)]
    cnt = 0
    res = 0
    while cnt < n:
        now_key, now_node = heapq.heappop(q)
        if visited[now_node]: continue
        visited[now_node] = True
        cnt += 1
        if now_key: 
            res += now_key + (t * (cnt-2))               
        for next_node, next_key in G[now_node]:
            heapq.heappush(q, (next_key, next_node))
    return res

n , m , t = map(int, input().split())
G = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    G[a].append((b, c))
    G[b].append((a, c))
print(prim(1,0))