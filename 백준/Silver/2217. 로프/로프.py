import sys
input = sys.stdin.readline

n = int(input())
ropes = []
for _ in range(n): ropes.append(int(input()))
ropes.sort(reverse=True)

res = 0
for i in range(1, n+1):
    res = max(res,ropes[i-1] * i)
    
print(res)