import sys
input = sys.stdin.readline

n , c = map(int, input().split())
m = int(input())
box_list = []
for _ in range(m):
    start, end, count = map(int, input().split())
    box_list.append((start, end, count))
box_list.sort(key=lambda x: [x[1], x[0], -x[2]])
truck = [c] * (n+1)

res = 0
for start, end, count in box_list:
    max_available = min(truck[start:end])
    load =min(count, max_available)
    for i in range(start, end):
        truck[i] -= load
    res += load
print(res)