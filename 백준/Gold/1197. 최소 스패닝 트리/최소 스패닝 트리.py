import sys
input = sys.stdin.readline

import heapq

# heap = []
# heapq.heappush(heap, [50,1, 3])
# heapq.heappush(heap, [10,5,3])
# heapq.heappush(heap, [20])

# print(heap)
# print(heapq.heappop(heap)

def prim(start, weight):
    visited = [0] * (V+1)
    q = [[weight, start]]
    cnt = 0
    ans = 0
    while q:
        if cnt == V:
            break
        else:
            key , node = heapq.heappop(q)
            if visited[node]:
                continue
            else:
                cnt += 1
                ans += key
                visited[node] = 1
                for u , w in G[node]:
                    heapq.heappush(q, [w, u])
    return ans

V , E = map(int, input().split())
G = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    G[u].append([v, w])
    G[v].append([u, w])

print(prim(1, 0))