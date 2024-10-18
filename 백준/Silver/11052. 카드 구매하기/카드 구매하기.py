import sys
input = sys.stdin.readline

n = int(input())
P = list(map(int, input().split()))
P.insert(0,0)
length = len(P)

d = [0] * (10000+1)
d[1] = P[1]
for i in range(2, n+1):    
    for j in range(1, length):
        if i-j < 0 : break
        d[i] = max(d[i], d[i-j] + P[j])
print(d[n])