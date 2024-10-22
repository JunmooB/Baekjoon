import sys
input = sys.stdin.readline

n = int(input())
res = 0
length = len(str(n))
for i in range(length-1):
    temp = 9
    for j in range(i):
        temp *= 10
    res += temp * (i+1)
cnt = n - 10**(length-1) + 1
res += cnt * length

print(res)
# 1 * 9, 2 * 90, 3 * 900