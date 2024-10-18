import sys
input = sys.stdin.readline

n = int(input())
d = [0] *(10+1)
d[1] = 1
d[2] = 2
d[3] = 4
# d[n] = d[n-1] + d[n-2] + d[n-3]
for i in range(4, 11):
    d[i] = d[i-1] + d[i-2] + d[i-3]
for i in range(n):
    i = int(input())
    print(d[i])