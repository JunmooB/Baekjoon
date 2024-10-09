import sys
input = sys.stdin.readline

import heapq
def prim(start, weight):
    visited = [False] * (n+1)
    q = [[weight, start]]
    cnt = 0
    res = 0
    max_val = 0
    while q:
        if cnt == n: break
        key , node = heapq.heappop(q)
        if visited[node]: continue
        visited[node] = True
        cnt += 1
        res += key
        if key > max_val : max_val = key
        for next_node , next_weight in G[node]:
            if visited[next_node]: continue
            heapq.heappush(q, [next_weight, next_node])
    return res - max_val


n , m = map(int, input().split())
G = [[] for _ in range(n+1)]
for _ in range(m):
    a , b , c = map(int, input().split())
    if a == b: continue
    G[a].append((b, c))
    G[b].append((a, c))

print(prim(1,0))