import sys
input = sys.stdin.readline

n = int(input())
meetings = []
for _ in range(n):
    start , end = map(int, input().split())
    meetings.append((start, end))
meetings.sort(key=lambda x: (x[1], x[0]))

res = 0 
temp_end = 0
for start, end in meetings:
    if temp_end <= start:
        res += 1
        temp_end = end
print(res)