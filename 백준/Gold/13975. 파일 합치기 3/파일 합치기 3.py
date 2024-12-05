import sys
input = sys.stdin.readline

import heapq

t = int(input())
for _ in range(t):
    k = int(input())
    nums = list(map(int, input().split()))
    hp = []
    for num in nums:
        heapq.heappush(hp, num)
    temp = []
    res = 0
    while hp:
        temp_num = heapq.heappop(hp)
        temp.append(temp_num)

        if len(temp) == 2:
            res += sum(temp)
            heapq.heappush(hp, sum(temp))
            temp = []

    print(res)