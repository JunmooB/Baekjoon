import sys
input = sys.stdin.readline

import heapq

n , k = map(int, input().split())

juwelry_list = []
for _ in range(n):
    weight, value = map(int, input().split())
    heapq.heappush(juwelry_list, (weight, value))

bag_list = []
for _ in range(k):
    bag = int(input())
    bag_list.append(bag)
bag_list.sort()

res = 0
temp_val = []
for bag in bag_list:    
    while juwelry_list:
        if juwelry_list[0][0] <= bag:
            val = heapq.heappop(juwelry_list)[1]
            heapq.heappush(temp_val, -val)
        else:
            break
    if temp_val:
        res -= heapq.heappop(temp_val)
print(res)