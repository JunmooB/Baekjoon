import sys
input = sys.stdin.readline

from itertools import combinations
from bisect import bisect_left, bisect_right

n , c = map(int, input().split())
items = list(map(int, input().split()))
left_items = items[:n//2]
right_items = items[n//2:]

left_sums , right_sums = [], []

for i in range(1, len(left_items)+1):
    temp = combinations(left_items, i)
    for t in temp:
        left_sums.append(sum(t))

for i in range(1, len(right_items)+1):
    temp = combinations(right_items, i)
    for t in temp:
        right_sums.append(sum(t))
right_sums.sort()
res = 0
for left in left_sums:
    target = c - left
    res += bisect_right(right_sums, target) - bisect_left(right_sums, target)

res += left_sums.count(c)
res += right_sums.count(c)
print(res)