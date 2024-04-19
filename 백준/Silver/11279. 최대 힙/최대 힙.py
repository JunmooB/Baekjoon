import sys
input = sys.stdin.readline

import heapq

heap = []
res = []
n = int(input())
for i in range(n):
    num = int(input())
    if num > 0:
        heapq.heappush(heap, -num)
    else:
        if len(heap) == 0:
            res.append(0)
        else:
            res.append(-heapq.heappop(heap))
for val in res:
    print(val)