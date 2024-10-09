import sys
input = sys.stdin.readline

import heapq

def prim(start, weight):
    visited = [False] * n
    q = [[weight, start]]
    res = 0
    cnt = 0
    while cnt < n:
        now_key , now_node = heapq.heappop(q)
        if visited[now_node]: continue
        visited[now_node] = True
        res += now_key
        cnt += 1
        for next_node, next_key in G[now_node]:
            if visited[next_node]: continue
            heapq.heappush(q, [next_key, next_node])
    return res

while True:
    n , m = map(int, input().split())   
    if n ==0 and m == 0:
        break
    G = [[] for _ in range(n)]
    max_cost = 0
    for i in range(m):
        x, y , z = map(int, input().split())
        max_cost += z
        G[x].append((y, z))
        G[y].append((x, z))

    print(max_cost - prim(0, 0))