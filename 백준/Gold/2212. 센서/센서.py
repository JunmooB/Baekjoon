import sys
input = sys.stdin.readline

from itertools import combinations

n = int(input())
k = int(input())

if k >= n :
    print(0)
    exit()

nums = sorted(list(map(int, input().split())))

res_list = []
for i in range(len(nums)-1):
    res_list.append(nums[i+1] - nums[i])
    # print(nums[i+1] - nums[i], end = ' ')

res_list.sort(reverse=True)

for _ in range(k-1):
    res_list.pop(0)

print(sum(res_list))