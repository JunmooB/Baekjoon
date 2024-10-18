import sys
input = sys.stdin.readline

n = int(input())
P = list(map(int, input().split()))
P.insert(0,0)
length = len(P)

d = [1e9] * (1000+1)
d[0] = 0
d[1] = P[1]
# d[2] = min(P[1] *2, P[2])
for i in range(2, n+1):
    for j in range(1, i+1):
        d[i] = min(d[i], d[i-j] + P[j])
print(d[n])