import sys
input = sys.stdin.readline

import heapq
def prim(start, weight):
    visited = [False] * (n+1)
    q = [[weight, start]]
    cnt = 0
    res = 0
    while q:
        if cnt == n: break
        key , node = heapq.heappop(q)
        if visited[node]: continue
        visited[node] = True
        cnt += 1
        res += key
        for next_node , next_weight in G[node]:
            if visited[next_node]: continue
            heapq.heappush(q, [next_weight, next_node])
    if cnt != n:
        return -1
    else:
        return res


n , m = map(int, input().split())
G = [[] for _ in range(n+1)]
all_cost = 0
for _ in range(m):
    a , b , c = map(int, input().split())
    all_cost += c
    if a == b: continue
    G[a].append((b, c))
    G[b].append((a, c))

cost = prim(1,0)
if cost == -1:
    print(-1)
else:
    print(all_cost - cost)
