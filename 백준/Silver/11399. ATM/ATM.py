import sys
input = sys.stdin.readline

n = int(input())
times = list(map(int, input().split()))
times.sort()
res = 0
before_sum = 0
for time in times:
    res += before_sum + time
    before_sum += time
print(res)