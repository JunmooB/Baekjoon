import sys
input = sys.stdin.readline

from itertools import permutations

n , m = map(int, input().split())
nums = list(range(1,n+1))
permu_list = permutations(nums, m)
for permu in permu_list:
    print(*permu)