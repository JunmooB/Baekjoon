import sys
input = sys.stdin.readline

import heapq

n = int(input())
meetings = []
for _ in range(n):
    start , end = map(int, input().split())
    meetings.append((start, end))
meetings.sort(key=lambda x: [x[0], x[1]])

res_list = []
heapq.heappush(res_list, meetings[0][1])

for i in range(1, n):
    if meetings[i][0] >= res_list[0]:
        heapq.heappop(res_list)
        heapq.heappush(res_list, meetings[i][1])
    else:
        heapq.heappush(res_list, meetings[i][1])

print(len(res_list))