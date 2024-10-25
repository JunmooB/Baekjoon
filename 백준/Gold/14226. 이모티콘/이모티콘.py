import sys
input = sys.stdin.readline

from collections import deque

s = int(input())

visited = [[False] * 10001 for _ in range(10001)]
# 위치 node, clip, time
q = deque([(1, 0, 0)])
visited[1][0] = True

while q:
    now , clip, time = q.popleft()
    if now == s:
        print(time)
        break
    else:
        if not visited[now][now]:
            visited[now][now] = True
            q.append((now, now, time + 1))
        if not visited[now+clip][clip]:
            visited[now+clip][clip] = True
            q.append((now+clip, clip, time + 1))
        if not visited[now-1][clip]:
            visited[now-1][clip] = True
            q.append((now-1, clip, time + 1))
            
        