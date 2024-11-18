import sys
input = sys.stdin.readline

import heapq

n = int(input())
classes = []
for _ in range(n):
    start , end = map(int, input().split())
    classes.append((start, end))
classes.sort(key=lambda x: (x[0], x[1]))

heap = [classes[0][1]]
for i in range(1, n):
    if heap[0] <= classes[i][0]:
        heapq.heappop(heap)
    heapq.heappush(heap, classes[i][1])
print(len(heap))