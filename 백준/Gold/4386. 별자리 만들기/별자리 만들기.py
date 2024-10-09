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
    return res

def cal_distance(x , y):
    return (x ** 2 + y ** 2)**(1/2)

n = int(input())
star_list = []
for i in range(n):
    x , y = map(float, input().split())
    star_list.append((x, y))
G = [[] for _ in range(n+1)]
for i in range(n-1):
    for j in range(i+1, n):
        left_x , left_y = star_list[i][0] , star_list[i][1]
        right_x , right_y = star_list[j][0] , star_list[j][1]
        distance = cal_distance(left_x-right_x , left_y-right_y)
        G[i+1].append((j+1, distance))
        G[j+1].append((i+1, distance))       

print(prim(1, 0))