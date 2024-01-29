import sys
input = sys.stdin.readline

from collections import deque

f , s, g, u ,d = map(int, input().split())
q = deque([s])
visited= [0] * (f+1)
visited[s] = 1
while q:
    n = q.popleft()
    if n == g:
        print(visited[n]-1)
        exit(0)
    else:
        if 1<=n+u<=f and visited[n+u] == 0:
            q.append(n+u)
            visited[n+u] = visited[n] + 1
        if 1<=n-d<=f and visited[n-d] == 0:
            q.append(n-d)
            visited[n-d] = visited[n] + 1
print("use the stairs")