import sys
input = sys.stdin.readline

from itertools import combinations

n , c = map(int, input().split())
items = list(map(int, input().split()))
left_items = items[:n//2]
right_items = items[n//2:]

left_sums , right_sums = [], []

for i in range(len(left_items)+1):
    temp = combinations(left_items, i)
    for t in temp:
        left_sums.append(sum(t))

for i in range(len(right_items)+1):
    temp = combinations(right_items, i)
    for t in temp:
        right_sums.append(sum(t))
right_sums.sort()

res = 0

for left in left_sums:
    cnt = 0
    if left > c: continue

    s = 0
    e = len(right_sums)-1    
    while s <= e:
        mid = (s + e) // 2
        if left + right_sums[mid] > c:
            e = mid - 1
        else:
            # cnt = s
            s = mid + 1
    cnt = e
    # print(left, cnt, right_sums[cnt])
    res += cnt + 1

print(res)