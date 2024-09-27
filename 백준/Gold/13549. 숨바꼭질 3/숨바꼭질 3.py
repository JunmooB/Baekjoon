import sys
input = sys.stdin.readline

from collections import deque

n , k = map(int, input().split())
lines = [1e9] * (int(1e5) + 1)

lines[n] = 0
q = deque([n])
res = []
while q:
    now = q.popleft()
    if now == k:
        res.append(lines[now])
        # print(lines[now])
        # break
    else:
        if 0<= now-1 <=int(1e5) :
            if lines[now] + 1 < lines[now-1]:
                lines[now-1] = lines[now] + 1
                q.append(now-1)
        if 0<= now+1 <=int(1e5):
            if lines[now] + 1 < lines[now+1]:
                lines[now+1] = lines[now] + 1
                q.append(now+1)
        if 0<= now*2 <=int(1e5):
            if lines[now] < lines[now*2]:
                lines[now*2] = lines[now]
                q.append(now*2)
print(min(res))
