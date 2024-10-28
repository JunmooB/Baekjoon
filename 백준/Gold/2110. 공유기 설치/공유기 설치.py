import sys
input = sys.stdin.readline
from math import sqrt

n , m = map(int, input().split())
positions = []
for i in range(n): positions.append(int(input()))
positions.sort()

s , e = 1, positions[n-1]
res = 0 
while s <= e:
    mid = (s+e) // 2
    cnt = 1
    temp_plus = 0
    for i in range(1, n):
        if positions[i] - positions[i-1] + temp_plus >= mid:
            cnt += 1
            temp_plus = 0
        else:
            temp_plus += positions[i] - positions[i-1]
    if cnt >= m:
        res = mid
        s = mid + 1
    else:
        e = mid -1
print(res)