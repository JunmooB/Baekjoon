import sys
input = sys.stdin.readline

from collections import deque

n , k = map(int, input().split())
q = deque([n])

Max = 10 ** 5
dist = [0] * (Max + 1)

while q:
    x = q.popleft()
    if x == k:
        print(dist[x])
        break
    for i in (x-1, x+1, x*2):
        if 0<=i<Max+1 and not dist[i]:
            dist[i] = dist[x] + 1
            q.append(i)