import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

from collections import deque

def print_history(num):
    global res
    if num == Max + 1:
        return
    else:
        res.append(num)
        print_history(visited[num])
    return

n , k = map(int, input().split())
q = deque([n])

Max = 10 ** 5
dist = [0] * (Max + 1)
dist[n] = 1
visited=[-1] * (Max +1)
visited[n] = Max + 1

while q:
    x = q.popleft()
    if x == k:
        print(dist[x]-1)
        break
    for i in (x-1, x+1, x*2):
        if 0<=i<Max+1 and not dist[i]:
            dist[i] = dist[x] + 1
            visited[i] = x
            q.append(i)
res = [k]            
print_history(visited[k])
res.reverse()
print(*res)