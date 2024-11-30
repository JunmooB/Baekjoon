import sys
input = sys.stdin.readline

import heapq

n = int(input())
if n == 0:
    print(0)
    exit()
lectures = []
for _ in range(n):
    p , d = map(int, input().split())
    heapq.heappush(lectures, (-p , d))

max_day = max(lectures, key=lambda x: x[1])[1]
assign_day = [0] * (max_day + 1)

for _ in range(n):
    p , d =heapq.heappop(lectures)
    for i in range(d, 0 , -1):
        if not assign_day[i]:
            assign_day[i] = -p
            break
print(sum(assign_day))