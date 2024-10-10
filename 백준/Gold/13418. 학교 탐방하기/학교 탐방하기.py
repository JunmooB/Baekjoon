import sys
input = sys.stdin.readline

import heapq

def worst_prim(start, weight):
    visited = [False] * (n+1)
    q = [(weight, start)]
    cnt = 0
    worse_cnt = 0
    while cnt < n+1:
        now_key , now_node = heapq.heappop(q)
        if visited[now_node]: continue
        visited[now_node] = True
        if now_key == 0:
            worse_cnt += 1
        cnt+=1
        for next_node, next_key in G[now_node]:
            heapq.heappush(q, (next_key, next_node))
    return worse_cnt - 1

def best_prim(start, weight):
    visited = [False] * (n+1)
    q = [(weight, start)]
    cnt = 0
    worse_cnt = 0
    while cnt < n+1:
        now_key , now_node = heapq.heappop(q)
        if visited[now_node]: continue
        visited[now_node] = True
        if now_key == 0:
            worse_cnt += 1
        cnt+=1
        for next_node, next_key in G[now_node]:
            heapq.heappush(q, (-next_key, next_node))
    return worse_cnt - 1
        

n , m = map(int, input().split())
G = [[] for _ in range(n+1)]
for i in range(m+1):    
    a , b, c = map(int, input().split())
    G[a].append([b, c])
    G[b].append([a, c])
w_num = worst_prim(0,0)
b_num = best_prim(0,0)
result = (w_num)**2 - (b_num)**2
print(abs(result))