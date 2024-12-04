import sys
input = sys.stdin.readline

import math

n , l = map(int, input().split())
water_holes = []
for _ in range(n):
    start , end = map(int, input().split())
    water_holes.append([start, end])
water_holes.sort(key=lambda x : x[0])

res = 0
covered_end = 0
for start, end in water_holes:
    if covered_end < start:
        covered_end = start

    if covered_end < end:
        length = end - covered_end
        cnt = math.ceil(length / l)
        res += cnt
        covered_end += cnt *l
print(res)