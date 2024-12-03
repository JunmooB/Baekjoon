import sys
input = sys.stdin.readline

import heapq

n = int(input()) 
lectures = []
cnt = 0
for i in range(n):
    _, start, end = map(int, input().split())
    lectures.append((start, end))
lectures.sort(key=lambda x: [x[0], x[1]])
res_list = []
heapq.heappush(res_list, lectures[0][1])

# print(lectures)
res = 1
for i in range(1, n):
    # print(res_list)
    if res_list[0] <= lectures[i][0]:
        heapq.heappop(res_list)
        heapq.heappush(res_list, lectures[i][1])
    else:
        heapq.heappush(res_list, lectures[i][1])
    res = max(res, len(res_list))
# print(res_list)
print(res)