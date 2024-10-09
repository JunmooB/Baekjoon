import sys
input = sys.stdin.readline

import heapq
def prim(start, weight):
    visited = [False] * (n)
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

def cal_distance_append(left_star, right_star):
    distance = right_star[0] - left_star[0]
    left_node , right_node = left_star[1] , right_star[1]
    G[left_node].append((right_node, distance))
    G[right_node].append((left_node, distance))    


n = int(input())
x_star , y_star, z_star = [] , [] , []
for i in range(n):
    x , y , z = map(int, input().split())
    x_star.append((x, i))
    y_star.append((y, i))
    z_star.append((z, i))
x_star.sort(), y_star.sort(), z_star.sort()

G = [[] for _ in range(n)]
for i in range(n-1):
    cal_distance_append(x_star[i], x_star[i+1])
    cal_distance_append(y_star[i], y_star[i+1])
    cal_distance_append(z_star[i], z_star[i+1])

print(prim(0,0))