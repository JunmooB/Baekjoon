import sys
input = sys.stdin.readline

import heapq

n = int(input())
heap = []
for _ in range(n):
    num = int(input())
    if num == 0:
        if len(heap) == 0:
            print(0)
        else:
            temp = heapq.heappop(heap)
            print(temp)
    else:
        heapq.heappush(heap, num)