import sys
input = sys.stdin.readline

from collections import deque, defaultdict

def bfs(left, right, refer_point):
    q = deque([left])
    visited = [False] * (n+1)
    visited[left] = True
    while q:
        node = q.popleft()
        if node == right:
            return True
        for next_key , next_node in edges[node]:
            if not visited[next_node] and next_key >= refer_point:
                visited[next_node] = True
                q.append(next_node)
        # for i in range(1,n+1):
        #     if not visited[i] and edges[node][i] >= refer_point:
        #         visited[i] = True
        #         q.append(i)

    return False 

n , m = map(int, input().split())
# edges = [[0] * (n+1) for _ in range(n+1)]
edges = [[] for _ in range(n+1)]
for i in range(m):
    a , b , c = map(int, input().split())
    # if edges[a][b] < c: edges[a][b] = edges[b][a] = c
    edges[a].append((c, b))
    edges[b].append((c, a))
for i in range(1,n+1):
    edges[i].sort(reverse=True)
fac_left , fac_right = map(int, input().split())

s = 1
e = int(1e9)
res = 0
while s <= e:
    mid = (s+e) // 2
    if bfs(fac_left, fac_right, mid):
        res = mid
        s = mid + 1
    else:
        e = mid -1
print(res) 