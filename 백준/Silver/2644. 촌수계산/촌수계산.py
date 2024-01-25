import sys
input = sys.stdin.readline

from collections import deque

n = int(input())
target_a , target_b = map(int, input().split())
m = int(input())

graph = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    parent , child = map(int, input().split())
    graph[parent][child] = graph[child][parent] = 1

visited = [0] * (n+1)
visited[target_a] = 1
def bfs(target_a):
    q = deque([target_a])
    while q:
        x = q.popleft()
        if x == target_b:
            return visited[x] - 1
        for ind, y in enumerate(graph[x]):
            if y == 1 and visited[ind] == 0:
                visited[ind] += visited[x] + 1
                q.append(ind)
    return -1
    
print(bfs(target_a))